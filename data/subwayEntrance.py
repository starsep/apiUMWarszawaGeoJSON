from data.wfsDownloader import WFSDownloader


class SubwayEntranceDownloader(WFSDownloader):
    def wfsId(self) -> str:
        return "0ac7f6d1-a26b-430f-9e3d-a41c5356b9a3"

    def outputFilename(self) -> str:
        return "subwayEntrance.geojson"
