from . import PaymentData
from . import Trip
from . import Flights
from . import Bank


class User:

    # id_user = Identificador usuario
    # email = Email
    # phone = Teléfono
    # payment_data = Información de pago (objeto de la clase PaymentData)
    def __init__(self, id_user, email, phone, payment_data: PaymentData):
        self.id_user = id_user
        self.email = email
        self.phone = phone
        self.payment_data = payment_data

    def pay(self, trip: Trip):
        price = trip.price
        self.payment_data.price = price

        bank = Bank()
        if bank.do_payment(self, self.payment_data):
            return True
        else:
            return False

    def Confirmar_Vol(self, flight : Flights):
        if flight.num_passengers != 'None' or flight.destination != 'None' or flight.id_flight != 'None':
            return False
        else:
            return True
