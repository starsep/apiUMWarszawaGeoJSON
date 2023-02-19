from data.wfsDownloader import WFSDownloader


class PoliceDownloader(WFSDownloader):
    def wfsId(self) -> str:
        return "85f567f1-bb56-4657-a30e-afd80544fc7f"

    def outputFilename(self) -> str:
        return "police.geojson"
