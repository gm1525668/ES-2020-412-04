import Trip


def TestGestionarNumeroViajeros(v):
    if v.num_passengers < 1:
        print("Viaje sin viajeros")
    else:
        print("Numero de viajeros = " + str(v.num_passengers))
        return v.num_passengers

def TestGestionarVariosDestinos(v):
    print ("Lista de destinos = " + str(v.destination))
    return v.destination



def main():

    v1 = Trip.Trip(20,0,['Paris', 'Ibiza', 'Roma'],0,0,0)
    v2 = Trip.Trip(5,0,['Berlín', 'Roma', 'Londres', 'Madrid'],0,0,0)
    v3 = Trip.Trip(10,0,['Atenas', 'Ibiza'],0,0,0)
    v4 = Trip.Trip(0,0,[],0,0,0)
    v5 = Trip.Trip(15,0,['Ibiza'],0,0,0)

    print("Test Gestionar Numero de Viajeros:")
    print("--------------------------------------------------------------------------------------------")
    TestGestionarNumeroViajeros(v1)
    TestGestionarNumeroViajeros(v2)
    TestGestionarNumeroViajeros(v3)
    TestGestionarNumeroViajeros(v4)
    TestGestionarNumeroViajeros(v5)

    print("--------------------------------------------------------------------------------------------")

    print("Test Gestionar Varios Destinos:")
    print("--------------------------------------------------------------------------------------------")
    TestGestionarVariosDestinos(v1)
    v1.add_destination('Atenas')
    TestGestionarVariosDestinos(v1)
    TestGestionarVariosDestinos(v4)
    TestGestionarVariosDestinos(v5)
    v5.remv_destination('NY')
    TestGestionarVariosDestinos(v5)
    print("--------------------------------------------------------------------------------------------")



if __name__ == "__main__":
    main()
