class PaymentData:

    # card_type = Tipo de tarjeta (VISA o Mastercard)
    # owner = Titular de la tarjeta
    # num = Número de tarjeta
    # security_code = Código de seguridad
    # price = Importe
    def __init__(self, card_type, owner, num, security_code, price):
        self.card_type = card_type
        self.owner = owner
        self.num = num
        self.security_code = security_code
        self.price = price

    def check_data(self):
        if self.card_type != 'VISA' and self.card_type != 'Mastercard':
            print('Error: Tipo de tarjeta no válido.')
            return False
        else:
            print('Ok: Tipo de tarjeta válido.')

        if self.owner is None:
            print('Error: Titular de tarjeta no válido.')
            return False
        else:
            print('Ok: Titular de tarjeta válido.')

        if not self.num.isnumeric() and len(self.num) != 16:
            print('Error: Número de tarjeta no válido.')
            return False
        else:
            print('Ok: Número de tarjeta válido.')

        if not self.num.isnumeric() and len(self.num) != 4:
            print('Error: Código de seguridad no válido.')
            return False
        else:
            print('Ok: Código de seguridad válido.')

        if not self.num.isnumeric() and self.price >= 0:
            print('Error: Importe no válido.')
            return False
        else:
            print('Ok: Importe válido.')

        return True
