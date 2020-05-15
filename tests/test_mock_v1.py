import unittest
from src.Trip import Trip
from unittest import mock


class TestPayment(unittest.TestCase):
    @mock.patch('src.User')
    def test_payment(self, mock_user):
        # set up mock
        self.assertTrue(mock_user.pay(Trip(2,'barna','callesalamanca', 0, 0, 100)))
        mock_user.pay.return_value = False
        self.assertFalse(mock_user.pay(Trip(2,'barna','callesalamanca', 0, 0, 100)))


if __name__ == '__main__':
    unittest.main()
