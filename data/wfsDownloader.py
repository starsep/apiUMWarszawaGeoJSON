import json
from abc import ABC, abstractmethod

import geojson
from geojson import FeatureCollection, Point, Feature, LineString

from data.dataDownloader import DataDownloader


class WFSDownloader(DataDownloader, ABC):
    def download(self) -> FeatureCollection:
        data = self.downloadJSON()
        output = []
        parsed = geojson.loads(json.dumps(data["result"]["featureMemberList"]))
        for feature in parsed:
            properties = {prop["key"]: prop["value"] for prop in feature["properties"]}
            if feature["geometry"]["type"] == "ShapePoint":
                coord = feature["geometry"]["coordinates"][0]
                output.append(
                    Feature(
                        geometry=Point(
                            (float(coord["longitude"]), float(coord["latitude"]))
                        ),
                        properties=properties,
                    )
                )
            elif feature["geometry"]["type"] == "ShapeLinearString":
                output.append(
                    Feature(
                        geometry=LineString(
                            [
                                (float(coord["longitude"]), float(coord["latitude"]))
                                for coord in feature["geometry"]["coordinates"]
                            ]
                        ),
                        properties=properties,
                    )
                )
            elif feature["geometry"]["type"] == " ShapeMultiLineString":
                # TODO: MultiLineString is broken. I see no way of establishing what is line within data
                pass
        return FeatureCollection(output)

    @abstractmethod
    def wfsId(self) -> str:
        raise NotImplementedError

    def downloadUrl(self):
        return f"https://api.um.warszawa.pl/api/action/wfsstore_get?id={self.wfsId()}&apikey={self.apiKey}"
