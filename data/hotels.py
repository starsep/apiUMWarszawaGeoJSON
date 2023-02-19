from data.wfsDownloader import WFSDownloader


class HotelDownloader(WFSDownloader):
    def wfsId(self) -> str:
        return "f019448f-951c-439e-bf37-c3268682752e"

    def outputFilename(self) -> str:
        return "hotel.geojson"
