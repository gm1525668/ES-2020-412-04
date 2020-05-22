import re
from . import PaymentData
from . import Trip
from src.Bank import Bank


EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


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
        trip.calc_price()
        self.payment_data.price = trip.price

        bank = Bank()
        if bank.do_payment(self, self.payment_data):
            return True
        else:
            print('Error: No se ha podido realizar el pago correctamente.')
            return False

    def set_data(self, email, phone, payment_data: PaymentData):
        if email is not None:
            if not EMAIL_REGEX.match(email):
                print('Error: Formato de email no válido.')
                return False
            else:
                print('Ok: Formato de email de teléfono válido.')
                self.email = email

        if phone is not None:
            if not str(phone).isnumeric() and len(phone) != 9:
                print('Error: Formato de número de teléfono no válido.')
                return False
            else:
                print('Ok: Formato de número de teléfono válido.')
                self.phone = phone

        if not payment_data.check_data():
            return False

        print('Ok: Datos de facturación completos.')
        return True
