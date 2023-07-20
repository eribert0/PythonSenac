class Quadrado:
    tamanho_do_lado = 0.0

    def Mudar_valor_do_lado(self, tamanhoLado):
        self.tamanho_do_lado = tamanhoLado

    def Retornar_valor_do_lado(self):
        return self.tamanho_do_lado
    
    def calcular_area(self):
        return self.tamanho_do_lado * self.tamanho_do_lado
    
    def __str__(self):
        return f'Quadrado do Usuário\nTamanho do lado do Quadrado: {self.tamanho_do_lado}\nÁrea do Quadrado: {self.calcular_area()}'
    
q1 = Quadrado()
q1.tamanho_do_lado = 5.0
print(q1)