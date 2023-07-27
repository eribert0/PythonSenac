class Processador:
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade

    def metodo_pro(self):
        return f'Processador: {self.modelo} - {self.velocidade}GHz'
