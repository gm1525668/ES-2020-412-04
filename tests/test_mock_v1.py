import unittest
from unittest import mock
from src.Trip import Trip
from src.Flights import Flight
from src.User import User


class TestPayment(unittest.TestCase):
    @mock.patch('src.User')
    def test_payment(self, mock_user):
        # set up mock
        trip = Trip(2, 'BCN', 'LDN', 0, 0, 100)
        self.assertTrue(mock_user.pay(trip))
        mock_user.pay.return_value = False
        self.assertFalse(mock_user.pay(trip))


class TestConfigVol(unittest.TestCase):
    @mock.patch('src.User')
    def test_ConfVol(self, mock_user):
        fly=Flight('AZ47-B', 'BCN', 'LDN')
        self.assertTrue(mock_user.Confirmar_Vol(fly))
        mock_user.Confirmar_Vol.return_value = False
        self.assertFalse(mock_user.Confirmar_Vol(fly))


if __name__ == '__main__':
    unittest.main()
