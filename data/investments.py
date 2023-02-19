from geojson import FeatureCollection, Feature, Point

from data.dataDownloader import DataDownloader


# TODO: no coordinates, district?
class InvestmentsDownloader(DataDownloader):
    def outputFilename(self) -> str:
        return "investments.geojson"

    def download(self) -> FeatureCollection:
        investments = self.downloadJSON()
        features = []
        for investmentList in investments["result"]["Items"].values():
            for investment in investmentList:
                investmentId = investment["ID"]
                investmentDetails = self.downloadJSON(
                    url=f"https://api.um.warszawa.pl/api/action/get_open_invest_details?resource_id=25feb40c-f26a-428b-89ba-27ffefa795a5&investId={investmentId}&apikey={self.apiKey}"
                )
        return FeatureCollection(features)

    def downloadUrl(self):
        return f"https://api.um.warszawa.pl/api/action/get_open_invests?resource_id=26b9ade1-f5d4-439e-84b4-9af37ab7ebf1&pageSize=5&StartIndex=4&apikey={self.apiKey}"
