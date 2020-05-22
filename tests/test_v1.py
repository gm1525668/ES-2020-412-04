import unittest
from unittest import mock
import pytest
from src.User import User
from src.PaymentData import PaymentData
from src.Trip import Trip
from src.Flights import Flights
from src.Hotels import Hotels
from src.Cars import Cars


@pytest.mark.parametrize('num_passengers, result', [(2, 2), (3, 3), (4, 4), (52, 52)])
def test_num_passengers(num_passengers, result):
    trip = Trip(num_passengers, 'BCN', [], '01/05/2020', '10/05/2020')
    assert trip.num_passengers == result


def test_no_destination_flight_list_empty():
    num_passengers = 2
    trip = Trip(num_passengers, 'BCN', [], '01/05/2020', '10/05/2020')
    assert trip.get_flights() == []


def test_no_destinations_price_zero():
    num_passengers = 2

    trip = Trip(num_passengers, 'BCN', [], '01/05/2020', '10/05/2020')
    trip.calc_price()

    assert trip.price == 0


def test_add_destination_flight_list():
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
        {'flight': flight5, 'hotel': None, 'car': None}
    ]

    trip = Trip(num_passengers, 'BCN', destination_list, '01/05/2020', '10/05/2020')
    trip.add_destination(flight4, hotel4, car4)

    result_flights_list = [flight1, flight2, flight3, flight4, flight5]
    assert trip.get_flights() == result_flights_list


def test_calc_price():
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
    trip.calc_price()

    result_price = 450
    assert trip.price == result_price


def test_add_destination_calc_price():
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
        {'flight': flight5, 'hotel': None, 'car': None}
    ]

    trip = Trip(num_passengers, 'BCN', destination_list, '01/05/2020', '10/05/2020')
    trip.add_destination(flight4, hotel4, car4)
    trip.calc_price()

    result_price = 450
    assert trip.price == result_price


def test_remove_destination_flight_list():
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
    trip.remove_destination(flight4, hotel4, car4)

    result_flights_list = [flight1, flight2, flight3, flight5]
    assert trip.get_flights() == result_flights_list


def test_remove_destination_calc_price():
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
    trip.remove_destination(flight4, hotel4, car4)
    trip.calc_price()

    result_price = 335
    assert trip.price == result_price


def test_confirm_pay():
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

    assert user.pay(trip)


class testPayment(unittest.TestCase):
    @mock.patch('src.User.Bank')
    def test_payment(self, mock_bank):
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

        mock_bank.return_value.do_payment.return_value = False
        self.assertFalse(user.pay(trip))


# ARREGLAR ESTA PUTA MIERDA
def test_confirm_flight():
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

    Confirm = trip.Confirmar_Vol(trip.get_flights())
    Result = True
    assert Confirm == Result


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