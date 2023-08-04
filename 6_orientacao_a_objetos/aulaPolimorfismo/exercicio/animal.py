class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print('Animal falando...')

    def imprimir(self):
        print(f'Nome: {self.nome}')

class Mamifero(Animal):
    def __init__(self, nome, corPelo):
        super().__init__(nome)
        self.corPelo = corPelo

    def imprimir(self):
        print(f'Cor do Pelo: {self.corPelo}')

class Voador(Animal):
    def __init__(self, nome, envergaduraAsas):
        super().__init__(nome)
        self.envergaduraAsas = envergaduraAsas

    def imprimir(self):
        print(f'Tem envergadura da Asa: {self.envergaduraAsas}')

m = Mamifero('cachorro', 'preto')
m.falar()
m.imprimir()

a = Animal('gato')
a.imprimir()

v = Voador('Pássaro', True)
v.falar()

class Cachorro(Mamifero):
    def __init__(self, nome, corPelo, raca):
        super().__init__(nome, corPelo)
        self.raca = raca

    def imprimir(self):
        print(f'Raça: {self.raca}')

    def falar(self):
        print('Cachorro está latindo...')


class Gato(Mamifero):
    