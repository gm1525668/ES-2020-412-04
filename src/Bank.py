from . import User
from . import PaymentData
#do nothing

class Bank:

    def __init__(self):
        pass

    def do_payment(self, user: User, payment_data: PaymentData):
        return True