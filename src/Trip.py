from . import User
from . import Flights
from . import Hotels
from . import Cars


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
            self.flight_list.insert((len(self.flight_list) - 1), flight)

            if hotel is not None and hotel not in self.hotel_list:
                self.hotel_list.append(hotel)

            if car is not None and car not in self.car_list:
                self.car_list.append(car)
        else:
            print('Destino ya seleccionado')

    def remove_destination(self, flight: Flights, hotel: Hotels, car: Cars):
        if flight in self.flight_list:
            self.flight_list.remove(flight)

            if hotel is not None and hotel in self.hotel_list:
                self.hotel_list.remove(hotel)

            if car is not None and car in self.car_list:
                self.car_list.remove(car)
        else:
            print('Destino no valido para eliminar')

    def calc_price(self):
        for flight in self.flight_list:
            self.price += flight.price

        for hotel in self.hotel_list:
            self.price += hotel.price

        for car in self.car_list:
            self.price += car.price

    def Confirmar_Vol(self, flight: Flights):
        Confirm = 0
        for counter, flight in enumerate(self.flight_list):
            if flight.num_passengers != 'None' or flight.destination != 'None' or flight.id_flight != 'None' or flight.price != 'None':
                print('No se ha podido confirmar la reserva de vuelo numero:' + counter)

            else:
                print('Confirmación Correcta')
                Confirm += 1
        if Confirm == len(self.flight_list):
            return True
        else:
            return False

    def reserve_flights(self, user: User):
        for flight in self.flight_list:
            if not flight.reserve_flight(user):
                print('Error: No se ha podido reservar el vuelo ' + str(flight.id_flight) + ' correctamente.')
                return False

        return True
