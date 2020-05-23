import pytest
import unittest
from unittest import mock
from datetime import date
from src.User import User
from src.PaymentData import PaymentData
from src.Trip import Trip
from src.Flights import Flights
from src.Hotels import Hotels
from src.Cars import Cars


@pytest.mark.parametrize('user_email, user_phone, user_payment_data, result', [
    ('should_not_work', 'should_not_work', PaymentData('VISA', 'Test', '4940190000370787', 1111, 0), False),
    ('should_not_work@gmail', 111222333, PaymentData('Mastercard', 'Test', '4940190000370787', 1111, 0), False),
    ('should_work@gmail.com', 111222333, PaymentData('should_not_work', 'Test', '4940190000370787', 1111, 0), False),
    ('should_work@gmail.com', 111222333, PaymentData('VISA', None, '4940190000370787', 1111, 0), False),
    ('should_work@gmail.com', 111222333, PaymentData('VISA', None, '494019000037078700000', 1111, 0), False),
    ('should_work@gmail.com', 111222333, PaymentData('VISA', None, 'should_not_work', 1111, 0), False),
    ('should_work@gmail.com', 111222333, PaymentData('VISA', None, '4940190000370787', 11110, 0), False),
    ('should_work@gmail.com', 111222333, PaymentData('VISA', None, '4940190000370787', 'xxxx', 0), False),
    ('should_work@gmail.com', 111222333, PaymentData('VISA', None, '4940190000370787', 1111, -5), False),
    ('should_work@gmail.com', 111222333, PaymentData('VISA', 'Test', '4940190000370787', 1111, 0), True)
])
def test_modify_user_data(user_email, user_phone, user_payment_data, result):
    payment_data = PaymentData('VISA', 'Test', '4940190000370787', 1111, 0)
    user = User(1, 'test@gmail.com', 111111111, payment_data)

    assert user.set_data(user_email, user_phone, user_payment_data) == result


class TestRetryHotels(unittest.TestCase):
    @mock.patch('src.Trip.Hotels.Booking')
    def test_retry_reserve_hotels(self, mock_booking):
        num_passengers = 2

        flight1 = Flights(1, 'BRE', num_passengers, 10)
        flight2 = Flights(2, 'BRU', num_passengers, 20)
        flight3 = Flights(3, 'MRS', num_passengers, 30)
        flight4 = Flights(4, 'DUB', num_passengers, 40)
        flight5 = Flights(5, 'BCN', num_passengers, 50)

        hotel1 = Hotels(1, 'Hotel 1', num_passengers, 1, 2, 50)
        hotel2 = Hotels(2, 'Hotel 2', num_passengers, 1, 2, 50)
        hotel3 = Hotels(3, 'Hotel 3', num_passengers, 1, 2, 50)
        hotel4 = Hotels(4, 'Hotel 4', num_passengers, 1, 2, 50)

        car1 = Cars(1, 'Honda', 'Airport', 2, 25)
        car2 = Cars(2, 'Audi', 'Airport', 2, 25)
        car3 = Cars(3, 'Mercedes', 'Airport', 2, 25)
        car4 = Cars(4, 'Mazda', 'Airport', 2, 25)

        destination_list = [
            {'flight': flight1, 'hotel': hotel1, 'car': car1, 'days': 3},
            {'flight': flight2, 'hotel': hotel2, 'car': car2, 'days': 2},
            {'flight': flight3, 'hotel': hotel3, 'car': car3, 'days': 3},
            {'flight': flight4, 'hotel': hotel4, 'car': car4, 'days': 2},
            {'flight': flight5, 'hotel': None, 'car': None, 'days': 0}
        ]

        payment_data = PaymentData('VISA', 'Test', '4940190000370787', 1111, 0)
        user = User(1, 'test@gmail.com', 111111111, payment_data)

        trip = Trip(num_passengers, 'BCN', destination_list, date(2020, 5, 1))

        mock_booking.return_value.confirm_reserve.return_value = False
        self.assertFalse(trip.reserve_hotels(user))

        mock_booking.return_value.confirm_reserve.return_value = True
        self.assertTrue(trip.reserve_hotels(user))


class TestRetryCars(unittest.TestCase):
    @mock.patch('src.Trip.Cars.Rentalcars')
    def test_retry_reserve_cars(self, mock_rentalcars):
        num_passengers = 2

        flight1 = Flights(1, 'BRE', num_passengers, 10)
        flight2 = Flights(2, 'BRU', num_passengers, 20)
        flight3 = Flights(3, 'MRS', num_passengers, 30)
        flight4 = Flights(4, 'DUB', num_passengers, 40)
        flight5 = Flights(5, 'BCN', num_passengers, 50)

        hotel1 = Hotels(1, 'Hotel 1', num_passengers, 1, 2, 50)
        hotel2 = Hotels(2, 'Hotel 2', num_passengers, 1, 2, 50)
        hotel3 = Hotels(3, 'Hotel 3', num_passengers, 1, 2, 50)
        hotel4 = Hotels(4, 'Hotel 4', num_passengers, 1, 2, 50)

        car1 = Cars(1, 'Honda', 'Airport', 2, 25)
        car2 = Cars(2, 'Audi', 'Airport', 2, 25)
        car3 = Cars(3, 'Mercedes', 'Airport', 2, 25)
        car4 = Cars(4, 'Mazda', 'Airport', 2, 25)

        destination_list = [
            {'flight': flight1, 'hotel': hotel1, 'car': car1, 'days': 3},
            {'flight': flight2, 'hotel': hotel2, 'car': car2, 'days': 2},
            {'flight': flight3, 'hotel': hotel3, 'car': car3, 'days': 3},
            {'flight': flight4, 'hotel': hotel4, 'car': car4, 'days': 2},
            {'flight': flight5, 'hotel': None, 'car': None, 'days': 0}
        ]

        payment_data = PaymentData('VISA', 'Test', '4940190000370787', 1111, 0)
        user = User(1, 'test@gmail.com', 111111111, payment_data)

        trip = Trip(num_passengers, 'BCN', destination_list, date(2020, 5, 1))

        mock_rentalcars.return_value.confirm_reserve.return_value = False
        self.assertFalse(trip.reserve_cars(user))

        mock_rentalcars.return_value.confirm_reserve.return_value = True
        self.assertTrue(trip.reserve_cars(user))
