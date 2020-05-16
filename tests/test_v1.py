import pytest
from src.User import Trip

"""class TestPayment(unittest.TestCase):
    def test_payment(self):
        # set up user
        payment = PaymentData.PaymentData('visa', 'guillem', 43, 56, 140)
        trip = Trip.Trip(2, 'BCN', 'LDN', 0, 0, 100)
        usu = User(7658, 'D@GMAIL.COM', 653648925, payment)
        self.assertTrue(usu.pay(Trip))"""


@pytest.mark.parametrize('n_pas, result', [(2, 2), (3, 3), (4, 4), (52, 52)])
def test_num_pas(n_pas, result):
    trip = Trip.Trip(n_pas, 'BCN', 'LDN', 0, 0, 100)
    assert trip.num_passengers == result


def test_no_destination():
    trip = Trip.Trip(1, 'BCN', [], 0, 0, 100)

    assert trip.destination == []


def test_no_destination_flights():
    return True
