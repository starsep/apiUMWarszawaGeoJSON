import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

import diskcache as diskcache
import geojson
import httpx
from diskcache import Cache
from geojson import FeatureCollection
from httpx import Response

DOWNLOAD_PHOTOS = False

outputDir = Path("output")
picturesDir = Path("pictures")
outputDir.mkdir(exist_ok=True)
picturesDir.mkdir(exist_ok=True)
cache = Cache("cache")


@cache.memoize()
def cachedDownload(url: str) -> Response:
    return httpx.get(url, follow_redirects=True)


class DataDownloader(ABC):
    def __init__(self, apiKey: str):
        self.apiKey = apiKey

    @abstractmethod
    def downloadUrl(self):
        raise NotImplementedError

    @abstractmethod
    def download(self) -> FeatureCollection:
        raise NotImplementedError

    @abstractmethod
    def outputFilename(self) -> str:
        raise NotImplementedError

    def downloadJSON(self, url: Optional[str] = None):
        if url is None:
            url = self.downloadUrl()
        return cachedDownload(url).json()

    def run(self):
        with Path(outputDir, self.outputFilename()).open("w") as f:
            geojson.dump(self.download(), f)
