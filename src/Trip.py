from src.Flights import Flights
from src.Hotels import Hotels
from src.Cars import Cars


class Trip:

    # num_passengers = Número de pasajeros
    # origin = Orígen
    # destination = Destino
    # start_date = Fecha de salida
    # finish_date = Fecha de llegada
    # price = Precio
    def __init__(self, num_passengers, origin, flight_list, hotel_list, car_list, start_date, finish_date, price):
        self.num_passengers = num_passengers
        self.origin = origin
        self.flight_list = flight_list
        self.hotel_list = hotel_list
        self.car_list = car_list
        self.start_date = start_date
        self.finish_date = finish_date
        self.price = price

    def add_destination(self, flight: Flights, hotel: Hotels, car: Cars):
        if flight not in self.flight_list:
            self.flight_list.append(flight)

            if hotel is not None & hotel not in self.hotel_list:
                self.flight_list.append(flight)

            if car is not None & car not in self.car_list:
                self.car_list.append(car)
        else:
            print('Destino ya seleccionado')

    def remove_destination(self, flight: Flights, hotel: Hotels, car: Cars):
        if flight in self.flight_list:
            self.flight_list.remove(flight)

            if hotel is not None & hotel in self.hotel_list:
                self.flight_list.remove(flight)

            if car is not None & car in self.car_list:
                self.car_list.remove(car)
        else:
            print('Destino no valido para eliminar')
