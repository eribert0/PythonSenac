class Bola:
    
    cor = ''
    circunferencia = 0.0
    material = ''

    def trocaCor(self, cor):
        self.cor = cor

    def mostrarCor(self):
        return self.cor

b1 = Bola()
b1.cor = 'Vermelho'
b1.circunferencia = 30.0
b1.material = 'poliuretano'
