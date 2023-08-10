from forma import Forma

class Retangulo(Forma):
    def __init__(self):
        super().__init__()
        self.base = int
        self.altura = int

    def areaRetangulo(self):
        print(f'Área: {self.base * self.altura}')

