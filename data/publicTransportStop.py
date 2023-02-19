from geojson import FeatureCollection, Feature, Point

from data.dataDownloader import DataDownloader


class PublicTransportStopDownloader(DataDownloader):
    def outputFilename(self) -> str:
        return "publicTransportStops.geojson"

    def download(self) -> FeatureCollection:
        stops = self.downloadJSON()
        features = []
        refToValues = dict()
        for stop in stops["result"]:
            values = {prop["key"]: prop["value"] for prop in stop["values"]}
            ref = values["zespol"] + values["slupek"]
            if (
                ref not in refToValues
                or values["obowiazuje_od"] > refToValues[ref]["obowiazuje_od"]
            ):
                refToValues[ref] = values
        for ref, values in refToValues.items():
            properties = dict(
                ref=ref,
                name=f"{values['nazwa_zespolu']} {values['slupek']}",
                update_date=values["obowiazuje_od"],
            )
            features.append(
                Feature(
                    properties=properties,
                    geometry=Point(
                        (float(values["dlug_geo"]), float(values["szer_geo"]))
                    ),
                )
            )
        return FeatureCollection(features)

    def downloadUrl(self):
        return f"https://api.um.warszawa.pl/api/action/dbstore_get?id=ab75c33d-3a26-4342-b36a-6e5fef0a3ac3&?apikey={self.apiKey}"
