from forma import Forma

PI = 3.14

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area_circulo(self):
        print(f'Área do círculo: {self.raio * self.raio * PI}')