from data.wfsDownloader import WFSDownloader


class TheaterDownloader(WFSDownloader):
    def wfsId(self) -> str:
        return "e26218cb-61ec-4ccb-81cc-fd19a6fee0f8"

    def outputFilename(self) -> str:
        return "theater.geojson"
