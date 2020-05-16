from src import User


def main():
    # precondition
    viaje = User.Trip.Trip(2, 'BCN', ['MDR'], [('BCN', 'VLC'), ('VLC', 'MDR'), ('MDR', 'BCN')], ['Fallas 5 estrelals', ])
    print('*El usuario pulsa el botón “Realizar pago de la reserva”*', '\n')
    print('*El usuario introduce sus datos de facturación*', '\n')




if __name__ == "__main__":
    main()
