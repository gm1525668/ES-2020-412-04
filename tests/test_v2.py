import pytest
from src.User import User
from src.PaymentData import PaymentData
from src.Trip import Trip
from src.Flights import Flights
from src.Hotels import Hotels
from src.Cars import Cars


@pytest.mark.parametrize('payment_method, result', [('VISA', 'VISA'), ('Mastercard', 'Mastercard')])
def test_payment_method(payment_method, result):
    num_passengers = 2

    flight1 = Flights(1, 'BRE', num_passengers, 10)
    flight2 = Flights(2, 'BRU', num_passengers, 20)
    flight3 = Flights(3, 'MRS', num_passengers, 30)
    flight4 = Flights(4, 'DUB', num_passengers, 40)
    flight5 = Flights(5, 'LDN', num_passengers, 50)
    flight6 = Flights(6, 'BCN', num_passengers, 60)

    flights_list = [flight1, flight2, flight3, flight4, flight5, flight6]

    hotel1 = Hotels(1, 'Hotel 1', num_passengers, 1, 2, 50)
    hotel2 = Hotels(2, 'Hotel 2', num_passengers, 1, 2, 50)
    hotel3 = Hotels(3, 'Hotel 3', num_passengers, 1, 2, 50)
    hotel4 = Hotels(4, 'Hotel 4', num_passengers, 1, 2, 50)

    hotels_list = [hotel1, hotel2, hotel3, hotel4]

    car1 = Cars(1, 'Honda', 'Airport', 2, 25)
    car2 = Cars(2, 'Audi', 'Airport', 2, 25)
    car3 = Cars(3, 'Mercedes', 'Airport', 2, 25)
    car4 = Cars(4, 'Mazda', 'Airport', 2, 25)

    cars_list = [car1, car2, car3, car4]

    trip = Trip(num_passengers, 'BCN', flights_list, hotels_list, cars_list, '01/05/2020', '10/05/2020', 0)

    payment_data = PaymentData(payment_method, 'Test', '4940190000370787', 1111, 0)
    user = User(1, 'test@gmail.com', 111111111, payment_data)
    user.pay(trip)

    assert user.payment_data.card_type == result


def test_pay_message_on_error():
    num_passengers = 2

    flight1 = Flights(1, 'BRE', num_passengers, 10)
    flight2 = Flights(2, 'BRU', num_passengers, 20)
    flight3 = Flights(3, 'MRS', num_passengers, 30)
    flight4 = Flights(4, 'DUB', num_passengers, 40)
    flight5 = Flights(5, 'LDN', num_passengers, 50)
    flight6 = Flights(6, 'BCN', num_passengers, 60)

    flights_list = [flight1, flight2, flight3, flight4, flight5, flight6]

    hotel1 = Hotels(1, 'Hotel 1', num_passengers, 1, 2, 50)
    hotel2 = Hotels(2, 'Hotel 2', num_passengers, 1, 2, 50)
    hotel3 = Hotels(3, 'Hotel 3', num_passengers, 1, 2, 50)
    hotel4 = Hotels(4, 'Hotel 4', num_passengers, 1, 2, 50)

    hotels_list = [hotel1, hotel2, hotel3, hotel4]

    car1 = Cars(1, 'Honda', 'Airport', 2, 25)
    car2 = Cars(2, 'Audi', 'Airport', 2, 25)
    car3 = Cars(3, 'Mercedes', 'Airport', 2, 25)
    car4 = Cars(4, 'Mazda', 'Airport', 2, 25)

    cars_list = [car1, car2, car3, car4]

    trip = Trip(num_passengers, 'BCN', flights_list, hotels_list, cars_list, '01/05/2020', '10/05/2020', 0)

    payment_data = PaymentData('VISA', 'Test', '4940190000370787', 1111, 0)
    user = User(1, 'test@gmail.com', 111111111, payment_data)

    assert user.pay(trip)


def test_reserve_flights_message_on_error():
    num_passengers = 2

    flight1 = Flights(1, 'BRE', num_passengers, 10)
    flight2 = Flights(2, 'BRU', num_passengers, 20)
    flight3 = Flights(3, 'MRS', num_passengers, 30)
    flight4 = Flights(4, 'DUB', num_passengers, 40)
    flight5 = Flights(5, 'LDN', num_passengers, 50)
    flight6 = Flights(6, 'BCN', num_passengers, 60)

    flights_list = [flight1, flight2, flight3, flight4, flight5, flight6]

    hotel1 = Hotels(1, 'Hotel 1', num_passengers, 1, 2, 50)
    hotel2 = Hotels(2, 'Hotel 2', num_passengers, 1, 2, 50)
    hotel3 = Hotels(3, 'Hotel 3', num_passengers, 1, 2, 50)
    hotel4 = Hotels(4, 'Hotel 4', num_passengers, 1, 2, 50)

    hotels_list = [hotel1, hotel2, hotel3, hotel4]

    car1 = Cars(1, 'Honda', 'Airport', 2, 25)
    car2 = Cars(2, 'Audi', 'Airport', 2, 25)
    car3 = Cars(3, 'Mercedes', 'Airport', 2, 25)
    car4 = Cars(4, 'Mazda', 'Airport', 2, 25)

    cars_list = [car1, car2, car3, car4]

    trip = Trip(num_passengers, 'BCN', flights_list, hotels_list, cars_list, '01/05/2020', '10/05/2020', 0)

    payment_data = PaymentData('VISA', 'Test', '4940190000370787', 1111, 0)
    user = User(1, 'test@gmail.com', 111111111, payment_data)

    assert trip.reserve_flights(user)