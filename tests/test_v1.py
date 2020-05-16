import unittest

from src.User import Trip
from src.User import User
from src.User import PaymentData



class TestPayment(unittest.TestCase):
    def test_payment(self):
        # set up user
        payment = PaymentData.PaymentData('visa', 'guillem', 43, 56, 140)
        trip = Trip.Trip(2, 'BCN', 'LDN', 0, 0, 100)
        usu = User(7658, 'D@GMAIL.COM', 653648925, payment)
        self.assertTrue(usu.pay(Trip))
