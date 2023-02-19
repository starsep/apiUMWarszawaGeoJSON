from data.wfsDownloader import WFSDownloader


class PharmacyDownloader(WFSDownloader):
    def wfsId(self) -> str:
        return "fd137190-3d65-4306-a85e-5e97e7f29a23"

    def outputFilename(self) -> str:
        return "pharmacy.geojson"
