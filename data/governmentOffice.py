from data.wfsDownloader import WFSDownloader


class GovernmentOfficeDownloader(WFSDownloader):
    def wfsId(self) -> str:
        return "4e9a942e-2bf8-4c9d-ac1f-1ccc30c4f62d"

    def outputFilename(self) -> str:
        return "governmentOffice.geojson"
