import base64
import os
from pathlib import Path

import geojson
import httpx
from geojson import Feature, FeatureCollection, Point
from tqdm import tqdm

API_UM_WARSZAWA_API_KEY = os.getenv("API_KEY")
DOWNLOAD_PHOTOS = False

outputDir = Path("output")
picturesDir = Path("pictures")
outputDir.mkdir(exist_ok=True)
picturesDir.mkdir(exist_ok=True)

aeds = httpx.get(
    f"https://api.um.warszawa.pl/api/action/aed_get/?apikey={API_UM_WARSZAWA_API_KEY}"
).json()
features = []
for aed in tqdm(aeds["result"]):
    properties = aed["properties"]
    aedId = properties["defibrillator_id"]
    properties["image"] = f"https://f003.backblazeb2.com/file/aedphotos/warszawaUM{aedId}.jpg"
    features.append(
        Feature(
            properties=properties, geometry=Point((aed["geometry"]["coordinates"][0]))
        )
    )
    if DOWNLOAD_PHOTOS:
        aedDetails = httpx.get(
            f"https://api.um.warszawa.pl/api/action/aed_get/?apikey={API_UM_WARSZAWA_API_KEY}&defibrillator_id={aedId}"
        ).json()
        properties = aedDetails["result"][0]["properties"]
        if "attachment" in properties:
            with Path(picturesDir / f"aed{aedId}.jpg").open("wb") as f:
                f.write(base64.b64decode(properties["attachment"]))

with (outputDir / "aed.geojson").open("w") as f:
    geojson.dump(FeatureCollection(features), f)
