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

    def add_destination(self, d):
        if d not in self.destination:
            self.destination.append(d)
        else:
            print('Destino ya seleccionado')

    def remove_destination(self, d):
        if d not in self.destination:
            print('Destino no valido para eliminar')
        else:
            self.destination.remove(d)
