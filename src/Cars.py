class Car:

    # id_car = Identificador coche
    # brand = Marca
    # place = Lugar de recogida
    # days = Duarada de la reserva (dias)
    def __init__(self, id_car, brand, place, days):
        self.id_car = id_car
        self.brand = brand
        self.place = place
        self.days = days


class Cars:

    def __init__(self, list_cars):
        self.list_cars = list_cars
