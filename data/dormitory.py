from data.wfsDownloader import WFSDownloader


class DormitoryDownloader(WFSDownloader):
    def wfsId(self) -> str:
        return "c789b05d-31b1-4b55-970a-4d3deb923f79"

    def outputFilename(self) -> str:
        return "dormitory.geojson"
