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
