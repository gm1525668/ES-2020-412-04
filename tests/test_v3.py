import unittest
from unittest import mock
from src.User import User
from src.PaymentData import PaymentData
from src.Trip import Trip
from src.Flights import Flights
from src.Hotels import Hotels
from src.Cars import Cars
def test_car_list():
    assert True == True  # quitar de lista
    assert True == True  # poner en la lista


def test_recalculate_price_trip_if_add_remove_car():
    assert True == True  # quitar de lista
    assert True == True  # poner en la lista

def test_hotel_list():
    assert True == True  # quitar de lista
    assert True == True  # poner en la lista


def test_recalculate_price_trip_if_add_remove_hotel():
    assert True == True  # quitar de lista
    assert True == True  # poner en la lista

# mock test, falta que este dentro de una clase, ojo
class testReserveCar(unittest.TestCase):
    @mock.patch('src.Trip.Rentalcars')
    def test_reserve_car(self,mock_Rentalcars):# se reserva
        num_passengers=2
        flight1 = Flights(1, 'BRE', num_passengers, 10)
        flight2 = Flights(2, 'BRU', num_passengers, 20)
        flight3 = Flights(3, 'MRS', num_passengers, 30)
        flight4 = Flights(4, 'DUB', num_passengers, 40)
        flight5 = Flights(5, 'LDN', num_passengers, 50)
        flight6 = Flights(6, 'BCN', num_passengers, 60)

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

        trip = Trip(num_passengers, 'BCN', destination_list, '01/05/2020', '10/05/2020', 0)
        payment_data = PaymentData('VISA', 'Test', '4940190000370787', 1111, 0)
        user = User(1, 'test@gmail.com', 111111111, payment_data)
        mock_Rentalcars.return_value.confirm_reserve.return_value = False
        self.assertFalse (trip.reserve_car(user))

# mock test, falta que este dentro de una clase, ojo


class testReserveHotel(unittest.TestCase):
    @mock.patch('src.User.Booking')
    def test_reserve_car(self, mock_Booking):  # se reserva
        num_passengers = 2
        flight1 = Flights(1, 'BRE', num_passengers, 10)
        flight2 = Flights(2, 'BRU', num_passengers, 20)
        flight3 = Flights(3, 'MRS', num_passengers, 30)
        flight4 = Flights(4, 'DUB', num_passengers, 40)
        flight5 = Flights(5, 'LDN', num_passengers, 50)
        flight6 = Flights(6, 'BCN', num_passengers, 60)

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

        trip = Trip(num_passengers, 'BCN', destination_list, '01/05/2020', '10/05/2020', 0)
        payment_data = PaymentData('VISA', 'Test', '4940190000370787', 1111, 0)
        user = User(1, 'test@gmail.com', 111111111, payment_data)
        mock_Booking.return_value.confirm_reserve.return_value = False
        self.assertFalse(trip.reserve_hotel(user))


    assert True == True  # se reserva
    assert False == False  # no se reserva

# con matriz de diferentes tests, iva, etc, echad un ojo a consideraciones del pdf
def test_calculate_price():
    assert True == True
    assert True == True
    assert True == True
    assert True == True
    assert True == True


