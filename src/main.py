from src import User


def main():
    # precondition
    viaje = User.Trip.Trip(2, 'BCN', ['MDR'], [('BCN', 'VLC'), ('VLC', 'MDR'), ('MDR', 'BCN')],
                           ['Fallas 5 estrelals', 'No hay playa 4 estrellas'], ['Seat ibiza', 'Seat Leon'],
                           '03/04/2020', '10/04/2020', 1400)
    print('*El usuario pulsa el botón “Realizar pago de la reserva”*', '\n')
    print('*El usuario introduce sus datos de facturación*', '\n')


if __name__ == "__main__":
    main()
