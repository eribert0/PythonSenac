class validacaoException(Exception):
    def __init__(self):
        super().__init__('Não é um triângulo')



class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC
        #print(f'O perímetro do triângulo é: {resultado}')

    def verificar_triangulo(self):
        if self.ladoA + self.ladoB <= self.ladoC or self.ladoB + self.ladoC <= self.ladoA or self.ladoA + self.ladoC <= self.ladoB:
            raise validacaoException()
        else:
            print('É um triângulo!')

try:
    t = Triangulo(10, 5, 5)
    print(f'Perímetro: {t.calcular_perimetro()}')
    t.verificar_triangulo()
except validacaoException as e:
    print(e)

