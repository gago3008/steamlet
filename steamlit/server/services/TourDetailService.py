from entities import Users
from repositories import UserRepository
from middlewares.securities import Security
from validate import schema
from config.configs import config_model
from api import UserSession, SessionMap
from repositories import TourDetailRepository
from services import TourDetailService
from common.convertDB import to_list

class TourService():
    security = Security(config_model)

    tourDetailRepository = TourDetailRepository()

    # tourDetailService = TourDetailService()

    def getTourDetailByTourId(self, tourId: int, skip:int = 0, limit:int = 100):
        listTourDetail = to_list(self.tourRepository.get_TourDetail(tourId, skip, limit))

        return listTourDetail


    def find_tour(self, tourname):
        try:
            listTour = to_list(self.tourRepository.get_Tour_byName(tourname))
            return listTour

        except:
            return list()