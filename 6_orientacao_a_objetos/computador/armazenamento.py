class Armazenamento:
    def __init__(self, tipo, capacidade):
        self.tipo = tipo
        self.capacidade = capacidade

    def metodo_arm(self):
        return f'Armazenamento: {self.tipo} - {self.capacidade}gb'