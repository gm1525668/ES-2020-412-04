from . import User
from . import Booking


class Hotels:

    # id_hotel = Identificador hotel
    # name = Nombre
    # num_guests = Número de huéspedes
    # num_rooms = Número de habitaciones
    # days = Duarada de la reserva (dias)
    # price = Precio
    def __init__(self, id_hotel, name, num_guests, num_rooms, days, price):
        self.id_hotel = id_hotel
        self.name = name
        self.num_guests = num_guests
        self.num_rooms = num_rooms
        self.days = days
        self.price = price

    def reserve_hotel(self, user: User):
        booking = Booking.Booking()
        if booking.confirm_reserve(user, self):
            return True
        else:
            return False




