from data.wfsDownloader import WFSDownloader


class ParkingParkAndRideDownloader(WFSDownloader):
    def wfsId(self) -> str:
        return "157648fd-a603-4861-af96-884a8e35b155"

    def outputFilename(self) -> str:
        return "parkingParkAndRide.geojson"
