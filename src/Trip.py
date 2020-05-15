class Trip:

    # num_passengers = Número de pasajeros
    # origin = Orígen
    # destination = Destino
    # start_date = Fecha de salida
    # finish_date = Fecha de llegada
    # price = Precio
    def __init__(self, num_passengers, origin, destination, start_date, finish_date, price):
        self.num_passengers = num_passengers
        self.origin = origin
        self.destination = destination
        self.start_date = start_date
        self.finish_date = finish_date
        self.price = price

    def add_destination(self, d):
        if d not in self.destination:
            self.destination.append(d)
        else:
            print('Destino ya seleccionado')



    def remv_destination(self, d):
        if d not in self.destination:
            print('Destino no valido para eliminar')
        else:
            self.destination.remove(d)

