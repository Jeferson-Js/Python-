class Conta: 
    def __init__(self,numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrado(self):
        print('O saldo {} do titular {}'.format(self.saldo, self.titular))

conta1 = Conta(106, "Jeferson", 1000, 10000)

conta1.extrado()