from entities import Users
from repositories import UserRepository
from middlewares.securities import Security
from validate import schema
from config.configs import config_model
from api import UserSession, SessionMap
from repositories import TourRepository, TourDetaiRepository
from services import TourDetailService
from common.convertDB import to_list

class TourService():
    security = Security(config_model)

    tourRepository = TourRepository()

    # tourDetailService = TourDetailService()

    def getTour(self, skip, limit):
        listTour = to_list(self.tourRepository.get_Tour(skip, limit))

        return listTour


    def find_tour(self, tourname):
        try:
            listTour = to_list(self.tourRepository.get_Tour_byName(tourname))
            return listTour

        except:
            return list()