import pytest
from src.User import User
from src.PaymentData import PaymentData
from src.Trip import Trip
from src.Flights import Flights
from src.Hotels import Hotels
from src.Cars import Cars

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


def test_add_destination():
    num_passengers = 2

    payment = PaymentData('VISA', 'Test', 4940190000370787, 1010, 0)
    user = User(1, 'test@gmail.com', 123456789, payment)

    flight1 = Flights(1, 'BRE', num_passengers)
    flight2 = Flights(2, 'BRU', num_passengers)
    flight3 = Flights(3, 'MRS', num_passengers)
    flight4 = Flights(4, 'DUB', num_passengers)
    flight5 = Flights(5, 'LDN', num_passengers)
    flight6 = Flights(6, 'BCN', num_passengers)

    flights_list = [flight1, flight2, flight3, flight4, flight5, flight6]

    hotel1 = Hotels(1, 'Hotel 1', num_passengers, 1, 2)
    hotel2 = Hotels(2, 'Hotel 2', num_passengers, 1, 2)
    hotel3 = Hotels(3, 'Hotel 3', num_passengers, 1, 2)
    hotel4 = Hotels(4, 'Hotel 4', num_passengers, 1, 2)

    hotels_list = [hotel1, hotel2, hotel3, hotel4]

    car1 = Cars(1, 'Honda', 'Airport', 2)
    car2 = Cars(2, 'Audi', 'Airport', 2)
    car3 = Cars(3, 'Mercedes', 'Airport', 2)
    car4 = Cars(4, 'Mazda', 'Airport', 2)

    cars_list = [car1, car2, car3, car4]

    trip = Trip(2, 'BCN', flights_list, hotels_list, cars_list, '01/05/2020', '10/05/2020', num_passengers, user)

    return True
