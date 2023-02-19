from data.wfsDownloader import WFSDownloader


class BicycleRouteDownloader(WFSDownloader):
    def wfsId(self) -> str:
        return "8a235d27-b96a-4876-9b92-9e164940c9b6"

    def outputFilename(self) -> str:
        return "bicycleRoute.geojson"
