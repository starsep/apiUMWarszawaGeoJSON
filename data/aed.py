import base64
from pathlib import Path

from geojson import Feature, FeatureCollection, Point
from tqdm import tqdm

from data.dataDownloader import DataDownloader, DOWNLOAD_PHOTOS, picturesDir


class AEDDownloader(DataDownloader):
    def outputFilename(self) -> str:
        return "aed.geojson"

    def download(self) -> FeatureCollection:
        aeds = self.downloadJSON()
        features = []
        for aed in tqdm(aeds["result"], leave=False):
            properties = aed["properties"]
            aedId = properties["defibrillator_id"]
            properties[
                "image"
            ] = f"https://f003.backblazeb2.com/file/aedphotos/warszawaUM{aedId}.jpg"
            features.append(
                Feature(
                    properties=properties,
                    geometry=Point((aed["geometry"]["coordinates"][0])),
                )
            )
            if DOWNLOAD_PHOTOS:
                aedDetails = self.downloadJSON(
                    self.downloadUrl() + f"&defibrillator_id={aedId}"
                )
                properties = aedDetails["result"][0]["properties"]
                if "attachment" in properties:
                    with Path(picturesDir / f"warszawaUM{aedId}.jpg").open("wb") as f:
                        f.write(base64.b64decode(properties["attachment"]))
        return FeatureCollection(features)

    def downloadUrl(self):
        return f"https://api.um.warszawa.pl/api/action/aed_get/?apikey={self.apiKey}"
