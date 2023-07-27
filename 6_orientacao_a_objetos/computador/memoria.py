class Memoria:
    def __init__(self, marca, capacidade):
        self.marca = marca
        self.capacidade = capacidade

    def metodo_mem(self):
        return f'Memória: {self.marca} - {self.capacidade}gb'