class Brinquedo:
    def __init__(self):
        self.tipo = str
        self.faixaE = str
        self.preco = float

    def ligar(self):
        print('O brinquedo está ligado!')

    def desligar(self):
        print('O brinquedo está desligado!')

    def imprimir(self):
        return f'Tipo: {self.tipo}\nFaixa: {self.faixaE}\nPreco: {self.preco}'