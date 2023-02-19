from data.wfsDownloader import WFSDownloader


class BicycleStationDownloader(WFSDownloader):
    def wfsId(self) -> str:
        return "d2f0c41f-cda1-440a-8a27-f01f724529f8"

    def outputFilename(self) -> str:
        return "bicycleStation.geojson"
