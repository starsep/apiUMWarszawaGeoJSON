import os
from typing import List, Callable

from tqdm import tqdm

from data.aed import AEDDownloader
from data.atmEuronet import ATMEuronetDownloader
from data.bicycleRoute import BicycleRouteDownloader
from data.bicycleStation import BicycleStationDownloader
from data.dataDownloader import DataDownloader
from data.dormitory import DormitoryDownloader
from data.governmentOffice import GovernmentOfficeDownloader
from data.hotels import HotelDownloader
from data.parkingParkAndRide import ParkingParkAndRideDownloader
from data.pharmacy import PharmacyDownloader
from data.police import PoliceDownloader
from data.publicTransportStop import PublicTransportStopDownloader
from data.subwayEntrance import SubwayEntranceDownloader
from data.theater import TheaterDownloader

API_UM_WARSZAWA_API_KEY = os.getenv("API_KEY")


def main():
    downloaders: List[Callable[[str], DataDownloader]] = [
        AEDDownloader,
        TheaterDownloader,
        BicycleStationDownloader,
        BicycleRouteDownloader,
        ParkingParkAndRideDownloader,
        SubwayEntranceDownloader,
        PublicTransportStopDownloader,
        GovernmentOfficeDownloader,
        PoliceDownloader,
        # TODO: Wfs error: IllegalArgumentException: FeatureMember list is empty
        # ATMEuronetDownloader,
        PharmacyDownloader,
        HotelDownloader,
        DormitoryDownloader,
    ]
    for downloader in tqdm(downloaders):
        downloader(API_UM_WARSZAWA_API_KEY).run()


if __name__ == "__main__":
    main()
