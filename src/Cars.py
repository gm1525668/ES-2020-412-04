from . import User
from . import Rentalcars

class Cars:

    # id_car = Identificador coche
    # brand = Marca
    # place = Lugar de recogida
    # days = Duarada de la reserva (dias)
    # price = Precio
    def __init__(self, id_car, brand, place, days, price):
        self.id_car = id_car
        self.brand = brand
        self.place = place
        self.days = days
        self.price = price

    def reserve_cars(self, user: User):
        rentalcars = Rentalcars.Rentalcars()
        if rentalcars.confirm_reserve(user, self):
            return True
        else:
            return False




