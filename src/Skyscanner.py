from . import User
from . import Flights
#do nothing

class Skyscanner():

    def __init__(self):
        pass

    def confirm_reserve(self, user: User, flights: Flights) -> bool:
        return True