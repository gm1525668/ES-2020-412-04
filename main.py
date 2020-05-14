import Trip


def TestGestionarNumeroViajeros(v):
    if v.num_passengers < 1:
        print("Viaje sin viajeros")
    else:
        print("Numero de viajeros = " + str(v.num_passengers))
        return v.num_passengers


def main():

    v1 = Trip.Trip(20,0,0,0,0,0)
    v2 = Trip.Trip(5,0,0,0,0,0)
    v3 = Trip.Trip(10,0,0,0,0,0)
    v4 = Trip.Trip(0,0,0,0,0,0)
    v5 = Trip.Trip(15,0,0,0,0,0)

    print("Test Gestionar Numero de Viajeros:")
    print("--------------------------------------------------------------------------------------------")
    TestGestionarNumeroViajeros(v1)
    TestGestionarNumeroViajeros(v2)
    TestGestionarNumeroViajeros(v3)
    TestGestionarNumeroViajeros(v4)
    TestGestionarNumeroViajeros(v5)

    print("--------------------------------------------------------------------------------------------")



if __name__ == "__main__":
    main()
