from src import User


def main():
    # precondition
    viaje = User.Trip.Trip(num_passengers=2, origin='BCN', flight_list=[('BCN', 'VLC'), ('VLC', 'MDR'), ('MDR', 'BCN')],
                           hotel_list=['Fallas 5 estrelals', 'No hay playa 4 estrellas'],
                           car_list=['Seat ibiza', 'Seat Leon'],
                           start_date='03/04/2020', finish_date='10/04/2020', price=1400)

    # flujo principal
    print('*El usuario pulsa el botón “Realizar pago de la reserva”*', '\n')
    datoscorrectos=False
    while(datoscorrectos==False):
        print('*El usuario introduce sus datos de facturación*', '\n')
        print('*El usuario pulsa continuar*', '\n')
        datospago = User.PaymentData.PaymentData(card_type='Visa', owner='Pepe', num=89539812515890, security_code=842,
                                                 price=viaje.price)
        usuario = User.User(id_user=1, email='pepe@gmail.com', phone=72419547, payment_data=datospago)

        print('*Validación de los datos*', '\n')
        if (datoscorrectos)
            datoscorrectos=True
        else:
            print('Datos de facturación incorrectos, vuelva a rellenar:')


if __name__ == "__main__":
    main()
