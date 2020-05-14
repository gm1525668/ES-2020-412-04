import Viaje


def main():

    print("Test Gestionar Numero de Viajeros:")
    print("--------------------------------------------------------------------------------------------")
    v1 = Viaje.Viaje(20)
    v2 = Viaje.Viaje(5)
    v3 = Viaje.Viaje(10)
    v4 = Viaje.Viaje(0)

    def TestGestionarNumeroViajeros(v):
        if v.get_viajeros() < 1:
            print("Viaje sin viajeros")
        else:
            print("Numero de viajeros = " + str(v.get_viajeros()))
            return v.get_viajeros()

    TestGestionarNumeroViajeros(v1)
    TestGestionarNumeroViajeros(v2)
    TestGestionarNumeroViajeros(v3)
    TestGestionarNumeroViajeros(v4)

    print("--------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
