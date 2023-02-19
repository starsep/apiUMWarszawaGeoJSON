from data.wfsDownloader import WFSDownloader


class ATMEuronetDownloader(WFSDownloader):
    def wfsId(self) -> str:
        return "672729a7-5ff9-45de-8ae2-ffc87213b9a8"

    def outputFilename(self) -> str:
        return "atmEuronet.geojson"
