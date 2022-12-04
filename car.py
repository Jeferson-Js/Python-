class Car:
    def __init__(self, marca, cor, preco):
        self.marca = marca
        self.cor = cor
        self.preco = preco

    def ligarOCarro(self):
        print('O carro esta ligado')  
        # Função responsavel por ligar o carro!

    def desligarOCarro(self):
        # Função responsavel por desligar o carro!
        print('O carro esta Desligado')

    def combustivel(self):
        # Função responsavel pela quantidade de gasolina!
        combustivelDoCarro = 100
        if combustivelDoCarro > 100:
            print('O carro esta com combustivel')
        else:
            print('O carro esta com pouco combustivel')


car_1 = Car('BMW', 'Branco', 'R$ 150.000')

car_1.ligarOCarro()
car_1.desligarOCarro()
car_1.combustivel()

print('A marca do seu carro é:' + car_1.marca)
print('A cor do seu carro é: ' + car_1.cor)
print('O valor pago pelo seu carro é de: ' + car_1.preco)
