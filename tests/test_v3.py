import unittest
from unittest import mock
from src.User import User
from src.PaymentData import PaymentData
from src.Trip import Trip
from src.Flights import Flights
from src.Hotels import Hotels
from src.Cars import Cars
from datetime import date


def test_car_list():
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
        {'flight': flight4, 'hotel': hotel4, 'car': None, 'days': 2},
        {'flight': flight5, 'hotel': None, 'car': None, 'days': 0}
    ]

    trip = Trip(num_passengers, 'BCN', destination_list, date(2020, 5, 1))

    trip.add_car(trip.get_destination_index(flight4), car4)

    result_cars_list = [car1, car2, car3, car4, None]
    assert trip.get_cars() == result_cars_list

    trip.remove_car(trip.get_destination_index(flight4), car4)

    result_cars_list = [car1, car2, car3, None, None]
    assert trip.get_cars() == result_cars_list


def test_recalculate_price_trip_if_add_remove_car():
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
        {'flight': flight4, 'hotel': hotel4, 'car': None, 'days': 2},
        {'flight': flight5, 'hotel': None, 'car': None, 'days': 0}
    ]

    trip = Trip(num_passengers, 'BCN', destination_list, date(2020, 5, 1))

    trip.add_car(trip.get_destination_index(flight4), car4)
    trip.calc_price()

    result_price = 450 * 1.16
    result_price = round(result_price, 2)

    assert trip.price == result_price

    trip.remove_car(trip.get_destination_index(flight4), car4)
    trip.calc_price()

    result_price = 425 * 1.16
    result_price = round(result_price, 2)

    assert trip.price == result_price


def test_hotel_list():
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
        {'flight': flight4, 'hotel': None, 'car': car4, 'days': 2},
        {'flight': flight5, 'hotel': None, 'car': None, 'days': 0}
    ]

    trip = Trip(num_passengers, 'BCN', destination_list, date(2020, 5, 1))

    trip.add_hotel(trip.get_destination_index(flight4), hotel4)

    result_hotel_list = [hotel1, hotel2, hotel3, hotel4, None]
    assert trip.get_hotels() == result_hotel_list

    trip.remove_hotel(trip.get_destination_index(flight4), hotel4)

    result_hotel_list = [hotel1, hotel2, hotel3, None, None]
    assert trip.get_hotels() == result_hotel_list


def test_recalculate_price_trip_if_add_remove_hotel():
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
        {'flight': flight4, 'hotel': None, 'car': car4, 'days': 2},
        {'flight': flight5, 'hotel': None, 'car': None, 'days': 0}
    ]

    trip = Trip(num_passengers, 'BCN', destination_list, date(2020, 5, 1))
    trip.add_hotel(trip.get_destination_index(flight4), hotel4)
    trip.calc_price()

    result_price = 450 * 1.16
    result_price = round(result_price, 2)

    assert trip.price == result_price

    trip.remove_hotel(trip.get_destination_index(flight4), hotel4)
    trip.calc_price()

    result_price = 400 * 1.16
    result_price = round(result_price, 2)

    assert trip.price == result_price


class TestReserveCar(unittest.TestCase):
    @mock.patch('src.Trip.Cars.Rentalcars')
    def test_reserve_car(self, mock_rentalcars):  # se reserva
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

        trip = Trip(num_passengers, 'BCN', destination_list, date(2020, 5, 1))

        payment_data = PaymentData('VISA', 'Test', '4940190000370787', 1111, 0)
        user = User(1, 'test@gmail.com', 111111111, payment_data)

        mock_rentalcars.return_value.confirm_reserve.return_value = True
        self.assertTrue(trip.reserve_cars(user))

        mock_rentalcars.return_value.confirm_reserve.return_value = False
        self.assertFalse(trip.reserve_cars(user))


class TestReserveHotel(unittest.TestCase):
    @mock.patch('src.Trip.Hotels.Booking')
    def test_reserve_hotel(self, mock_booking):
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

        trip = Trip(num_passengers, 'BCN', destination_list, date(2020, 5, 1))

        payment_data = PaymentData('VISA', 'Test', '4940190000370787', 1111, 0)
        user = User(1, 'test@gmail.com', 111111111, payment_data)

        mock_booking.return_value.confirm_reserve.return_value = True
        self.assertTrue(trip.reserve_hotels(user))

        mock_booking.return_value.confirm_reserve.return_value = False
        self.assertFalse(trip.reserve_hotels(user))


def test_calculate_price():
    num_passengers = 3

    flight1 = Flights(1, 'BRE', num_passengers, 10)
    flight2 = Flights(2, 'BRU', num_passengers, 20)
    flight3 = Flights(3, 'MRS', num_passengers, 30)
    flight4 = Flights(4, 'DUB', num_passengers, 40)
    flight5 = Flights(5, 'LDN', num_passengers, 50)

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

    trip = Trip(num_passengers, 'BCN', destination_list, date(2020, 5, 1))

    price_data = trip.calc_price()

    result = {'destination': [{'flight_total': 10, 'flight_person': 3.33, 'hotel_total': 50, 'hotel_day_person': 5.56,
                               'car_total': 25, 'car_day': 8.33},
                              {'flight_total': 20, 'flight_person': 6.67, 'hotel_total': 50, 'hotel_day_person': 8.33,
                               'car_total': 25, 'car_day': 12.50},
                              {'flight_total': 30, 'flight_person': 10, 'hotel_total': 50, 'hotel_day_person': 5.56,
                               'car_total': 25, 'car_day': 8.33},
                              {'flight_total': 40, 'flight_person': 13.33, 'hotel_total': 50, 'hotel_day_person': 8.33,
                               'car_total': 25, 'car_day': 12.50},
                              {'flight_total': 50, 'flight_person': 16.67, 'hotel_total': 0, 'hotel_day_person': 0,
                               'car_total': 0, 'car_day': 0}],
              'destination_total': [85, 95, 105, 115, 50],
              'trip_without_iva': 450,
              'iva_percentage': 0.16,
              'iva': 72,
              'trip_with_iva': 522
              }

    assert price_data['destination'] == result['destination']
    assert price_data['destination_total'] == result['destination_total']
    assert price_data['trip_without_iva'] == result['trip_without_iva']
    assert price_data['iva_percentage'] == result['iva_percentage']
    assert price_data['iva'] == result['iva']
    assert price_data['trip_with_iva'] == result['trip_with_iva']
