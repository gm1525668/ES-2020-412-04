from . import User
from src.Skyscanner import Skyscanner


class Flights:

    # id_flight = Identificador vuelo
    # destination = Destino
    # num_passengers = Número de pasajeros
    # price = Precio
    def __init__(self, id_flight, destination, num_passengers, price):
        self.id_flight = id_flight
        self.destination = destination
        self.num_passengers = num_passengers
        self.price = price

    def reserve_flight(self, user: User):
        skyscanner = Skyscanner()
        if skyscanner.confirm_reserve(user, self):
            return True
        else:
            return False
