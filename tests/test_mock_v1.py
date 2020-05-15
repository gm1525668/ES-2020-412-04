import unittest
from unittest import mock
from src.Trip import Trip
from src.User import User


class TestPayment(unittest.TestCase):
    @mock.patch('src.User')
    def test_payment(self, mock_user):
        # set up mock
        trip = Trip(2, 'BCN', 'LDN', 0, 0, 100)
        self.assertTrue(mock_user.pay(trip))
        mock_user.pay.return_value = False
        self.assertFalse(mock_user.pay(trip))


if __name__ == '__main__':
    unittest.main()
