import unittest
from unittest import mock
from src.User import User
from src.PaymentData import PaymentData
from src.Trip import Trip
from src.Flights import Flights
from src.Hotels import Hotels
from src.Cars import Cars


class testRetryPayment(unittest.TestCase):
    @mock.patch('src.User.Bank')
    def test_retry_payment(self, mock_bank):
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
            {'flight': flight1, 'hotel': hotel1, 'car': car1},
            {'flight': flight2, 'hotel': hotel2, 'car': car2},
            {'flight': flight3, 'hotel': hotel3, 'car': car3},
            {'flight': flight4, 'hotel': hotel4, 'car': car4},
            {'flight': flight5, 'hotel': None, 'car': None}
        ]

        trip = Trip(num_passengers, 'BCN', destination_list, '01/05/2020', '10/05/2020')
        payment_data = PaymentData('VISA', 'Test', '4940190000370787', 1111, 0)
        user = User(1, 'test@gmail.com', 111111111, payment_data)
        self.assertTrue(user.pay(trip))

        mock_bank.return_value.do_payment.return_value = False
        self.assertFalse(user.pay(trip))


class testRetryReserveFlights(unittest.TestCase):
    @mock.patch('src.Trip.Flights.Skyscanner')
    def test_retry_reserve_flight(self, mock_sky):
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
            {'flight': flight1, 'hotel': hotel1, 'car': car1},
            {'flight': flight2, 'hotel': hotel2, 'car': car2},
            {'flight': flight3, 'hotel': hotel3, 'car': car3},
            {'flight': flight4, 'hotel': hotel4, 'car': car4},
            {'flight': flight5, 'hotel': None, 'car': None}
        ]

        trip = Trip(num_passengers, 'BCN', destination_list, '01/05/2020', '10/05/2020')
        payment_data = PaymentData('VISA', 'Test', '4940190000370787', 1111, 0)
        user = User(1, 'test@gmail.com', 111111111, payment_data)
        self.assertTrue(trip.reserve_flights(user))

        mock_sky.return_value.confirm_reserve.return_value = False

        self.assertFalse(trip.reserve_flights(user))
