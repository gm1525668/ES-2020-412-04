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
    def __init__(self, num_passengers, origin, destination_list, start_date, finish_date):
        self.num_passengers = num_passengers
        self.origin = origin
        self.destination_list = destination_list
        self.start_date = start_date
        self.finish_date = finish_date
        self.price = 0

    def add_destination(self, flight: Flights, hotel: Hotels, car: Cars):
        if flight not in self.get_flights():
            self.destination_list.insert((len(self.destination_list) - 1),
                                         ({'flight': flight, 'hotel': hotel, 'car': car}))
        else:
            print('Error: El destino ya ha sido seleccionado anteriormente.')

    def remove_destination(self, flight: Flights, hotel: Hotels, car: Cars):
        if flight in self.get_flights():
            destination_to_remove = next((destination for destination in self.destination_list if destination['flight'] == flight), None)
            self.destination_list.remove(destination_to_remove)
        else:
            print('Error: El destino no existe en la lista de destinaciones.')

    def get_destination_index(self, flight: Flights):
        if flight in self.get_flights():
            index = next(
                (index for index, destination in enumerate(self.destination_list) if destination['flight'] == flight),
                None)
            return index

        return -1

    def get_flights(self):
        return [destination['flight'] for destination in self.destination_list]

    def get_hotels(self):
        return [destination['hotel'] for destination in self.destination_list]

    def get_cars(self):
        return [destination['car'] for destination in self.destination_list]

    def calc_price(self):
        self.price = 0
        for flight in self.get_flights():
            if flight is not None:
                self.price += flight.price

        for hotel in self.get_hotels():
            if hotel is not None:
                self.price += hotel.price

        for car in self.get_cars():
            if car is not None:
                self.price += car.price

    def Confirmar_Vol(self, flight: Flights):
        Confirm = 0
        for counter, flight in enumerate(flight):
            if flight.num_passengers != 0 and flight.destination != 'None' and flight.id_flight != 0 and flight.price != 0:
                print('Confirmación Correcta')
                Confirm += 1
            elif flight.num_passengers == 0:
                print('No se ha podido confirmar la reserva de vuelo numero:' + str(
                    counter) + 'debido a que no esta indicado en numero de pasajeros.')
            elif flight.destination == 0:
                print('No se ha podido confirmar la reserva de vuelo numero:' + str(
                    counter) + 'debido a que no esta indicada destinacion.')
            elif flight.id_flight == 0:
                print('No se ha podido confirmar la reserva de vuelo numero:' + str(
                    counter) + 'debido a que no esta indicada la id del vuelo.')
            elif flight.price == 0:
                print('No se ha podido confirmar la reserva de vuelo numero:' + str(
                    counter) + 'debido a que no esta indicado el precio.')
        if Confirm == len(self.get_flights()):
            return True
        else:
            return False

    def confirmar_coche(self, car: Cars):
        confirm = 0
        for counter, car in enumerate(self.get_cars()):
            if car.id_car != 0 and car.brand != 'None' and car.place != 0 and car.days != 0 and car.price != 0:
                print('Confirmación Correcta')
                confirm += 1
            elif car.id_car == 0:
                print('No se ha podido confirmar la reserva de coche numero:' + str(
                    counter) + 'debido a que no esta indicada la id del coche.')
            elif car.brand == 0:
                print('No se ha podido confirmar la reserva de coche numero:' + str(
                    counter) + 'debido a que no esta indicada la marca del coche.')
            elif car.place == 0:
                print('No se ha podido confirmar la reserva de coche numero:' + str(
                    counter) + 'debido a que no estan indicadas las plazas del coche.')
            elif car.days == 0:
                print('No se ha podido confirmar la reserva de coche numero:' + str(
                    counter) + 'debido a que no esta indicados los dias de alquiler del coche.')
            elif car.price == 0:
                print('No se ha podido confirmar la reserva de coche numero:' + str(
                    counter) + 'debido a que no esta indicado el precio del coche.')
        if confirm == len(self.get_cars()):
            return True
        else:
            return False

    def confirmar_hotel(self, hotel: Hotels):
        confirm = 0
        for counter, hotel in enumerate(self.get_hotels()):
            if hotel.id_hotel != 'None' and hotel.name != 'None' and hotel.num_guests != 0 and hotel.num_rooms != 0 and hotel.days != 0 and hotel.price != 0:
                print('Confirmación Correcta')
                confirm += 1
            elif hotel.id_hotel == 0:
                print('No se ha podido confirmar la reserva de hotel numero:' + str(
                    counter) + 'debido a que no esta indicada la id del hotel.')
            elif hotel.name == 0:
                print('No se ha podido confirmar la reserva de hotel numero:' + str(
                    counter) + 'debido a que no esta indicado el nombre del hotel.')
            elif hotel.num_guests == 0:
                print('No se ha podido confirmar la reserva de hotel numero:' + str(
                    counter) + 'debido a que no esta indicado el numero de personas que residiran en el hotel.')
            elif hotel.num_rooms == 0:
                print('No se ha podido confirmar la reserva de hotel numero:' + str(
                    counter) + 'debido a que no esta indicado el numero de habitaciones reservadas.')
            elif hotel.days == 0:
                print('No se ha podido confirmar la reserva de hotel numero:' + str(
                    counter) + 'debido a que no estan indicados los dias de la reserva.')
            elif hotel.price == 0:
                print('No se ha podido confirmar la reserva de hotel numero:' + str(
                    counter) + 'debido a que no esta indicado el precio del hotel.')
        if confirm == len(self.get_hotels()):
            return True
        else:
            return False

    def reserve_flights(self, user: User):
        for flight in self.get_flights():
            if not flight.reserve_flight(user):
                print('Error: No se ha podido reservar el vuelo ' + str(flight.id_flight) + ' correctamente.')
                return False

        print('Ok: Vuelos reservados correctamente.')
        return True

    def reserve_hotels(self, user: User):
        for hotel in self.get_hotels():
            if hotel is not None:
                attempts = 0
                check = hotel.reserve_hotel(user)
                while attempts < 1 and not check:
                    check = hotel.reserve_hotel(user)
                    attempts += 1

                if not check:
                    print('Error: No se ha podido reservar el hotel ' + str(hotel.id_hotel) + ' correctamente.')
                    return False

        print('Ok: Hoteles reservados correctamente.')
        return True

    def reserve_cars(self, user: User):
        for car in self.get_cars():
            if car is not None:
                attempts = 0
                check = car.reserve_car(user)
                while attempts < 1 and not check:
                    check = car.reserve_car(user)
                    attempts += 1

                if not check:
                    print('Error: No se ha podido reservar el coche ' + str(car.id_car) + ' correctamente.')
                    return False

        print('Ok: Coches reservados correctamente.')
        return True

    def add_car(self, n_dest, car: Cars):
        if car is not None and self.destination_list[n_dest]['car'] == None:
            self.destination_list[n_dest]['car']=car
        else:
            print('Este destino ya tiene un coche asignado')

    def remove_car(self, n_dest, car: Cars):
        if car is not None and self.destination_list[n_dest]['car'] != None:
            self.destination_list[n_dest]['car'] = None
        else:
            print('Este destino ya tiene un coche asignado')

    def add_hotel(self, n_destination, hotel: Hotels):
        if hotel is not None and self.destination_list[n_destination]['hotel'] == None:
            self.destination_list[n_destination]['hotel'] = hotel
        else:
            print('Este destino ya tiene un hotel asignado')

    def remove_hotel(self, n_destination, hotel: Hotels):
        if hotel is not None and self.destination_list[n_destination]['hotel'] != None:
            self.destination_list[n_destination]['hotel'] = None
        else:
            print('Este destino ya tiene un hotel asignado')
