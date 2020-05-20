
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
            if flight.num_passengers != 0 and flight.destination != 'None' and flight.id_flight != 0 and flight.price != 0:
                print('Confirmación Correcta')
                Confirm += 1
            else:
                print('No se ha podido confirmar la reserva de vuelo numero:' + str(counter))
        if Confirm == len(self.flight_list):
            return True
        else:
            return False
    def confirmar_coche(self, car: Cars):
        confirm = 0
        for counter, car in enumerate(self.car_list):
            if car.id_car != 0 and car.brand != 'None' and car.place != 0 and car.days != 0 and car.price != 0:
                print('Confirmación Correcta')
                confirm += 1
            else:
                print('No se ha podido confirmar la reserva del coche numero:' + str(counter))
        if confirm == len(self.car_list):
            return True
        else:
            return False

    def confirmar_hotel(self,hotel : Hotels):
        confirm = 0
        for counter, hotel in enumerate(self.hotel_list):
            if hotel.id_hotel != 'None' and hotel.name !='None' and  hotel.num_guests != 0 and hotel.num_rooms != 0 and hotel.days != 0 and hotel.price != 0:
                print('Confirmación Correcta')
                confirm += 1
            else:
                print('No se ha podido confirmar la reserva del Hotel  numero:' + str(counter))
        if confirm == len(self.hotel_list):
            return True
        else:
            return False





    def reserve_flights(self, user: User):
        for flight in self.flight_list:
            if not flight.reserve_flight(user):
                print('Error: No se ha podido reservar el vuelo ' + str(flight.id_flight) + ' correctamente.')
                return False

        return True



