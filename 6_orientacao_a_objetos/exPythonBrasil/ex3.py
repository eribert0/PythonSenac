class Retangulo:
    def __init__(self, ladoBase, ladoAltura):
        self.base = ladoBase
        self.altura = ladoAltura

    def mudar_valor_lados(self, valorBase, valorAltura):
        self.base = valorBase
        self.altura = valorAltura

    def retornar_valor_lados(self):
        return self.base, self.altura
    
    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (self.base + self.altura) * 2

    def __str__(self):
        return f'Valor da base: {self.base}\nValor da altura: {self.altura}\nValor perimetro: {self.calcular_perimetro()}\nValor área: {self.calcular_area()}'

r1 = Retangulo(10, 5)
print(r1)

