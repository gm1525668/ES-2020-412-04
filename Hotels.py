class Hotel:

    # id_hotel = Identificador hotel
    # name = Nombre
    # num_guests = Número de huéspedes
    # num_rooms = Número de habitaciones
    # days = Duarada de la reserva (dias)
    def __init__(self, id_hotel, name, num_guests, num_rooms, days):
        self.id_hotel = id_hotel
        self.name = name
        self.num_guests = num_guests
        self.num_rooms = num_rooms
        self.days = days


# list_hotels = Lista de hoteles

class Hotels:

    def __init__(self, list_hotels):
        self.list_hotels = list_hotels
