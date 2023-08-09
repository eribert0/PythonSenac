class Transporte:
    def __init__(self, nome):
        self.nome = nome 

    def imprimir(self):
        print(f'Nome: {self.nome}')

    def mover(self):
        print(f'O transporte está se movendo')

class Terrestre(Transporte):
    def __init__(self, nome, num_rodas):
        super().__init__(nome)
        self.num_rodas = num_rodas

    def imprimir(self):
        print(f'Numero de rodas: {self.num_rodas}')
              
    def mover(self):
        print('O transporte terrestre está se movendo')

    def dirigir(self):
        print(f'Transporte {self.nome} está em funcionamento sobre {self.num_rodas} rodas\n')

class Aereo(Transporte):
    def __init__(self, nome, comp_asas):
        super().__init__(nome)
        self.comp_asas = comp_asas


    def imprimir(self):
        print(f'Comprimento das asas: {self.comp_asas}')

    def mover(self):
        print('O transporte aéreo está se movendo')
    
    def voar(self):
        print(f'O transporte aéreo está voando com asas de comprimento {self.comp_asas} m\n')


class Maritimo(Transporte):
    def __init__(self, nome, porte):
        super().__init__(nome)
        self.porte = porte

    def imprimir(self):
        print(f'Porte: {self.porte}')

    def mover(self):
        print('O transporte aéreo está se movendo')

    def navegar(self):
        print(f'O trasporte maritimo de porte {self.porte} está navegando\n')


t = Transporte('Guanabara')
t.imprimir()
t.mover()

te = Terrestre('Honda', 2)
te.imprimir()
te.mover()
te.dirigir()

a = Aereo('Gol', 5.5)
a.imprimir()
a.mover()
a.voar()

#implementar classe carro

class Carro(Terrestre):
    def __init__(self, nome, num_rodas, modelo, cor):
        super().__init__(nome, num_rodas)
        self.modelo = modelo
        self.cor = cor

    def imprimir(self):
        super().imprimir()
        print(f'Modelo: {self.modelo}\nCor: {self.cor}')

    def mover(self):
        print(f'O carro está se movendo')

    def ligar(self):
        print(f'Carro ligado')

    def desligar(self):
        print(f'O carro está desligado!')

class Aviao(Aereo):
    def __init__(self, nome, comp_asas, num_assentos):
        super().__init__(nome, comp_asas)
        self.num_assentos = num_assentos

    def imprimir(self):
        super().imprimir()
        super().imprimir()
        print(f'Nº Assentos: {self.num_assentos}')

    def mover(self):
        print(f'Avião está se movendo')

    def decolar(self):
        print(f'O avião {self.nome} está decolando')

a = Aviao('Helicoptero', 7.2, 10)
a.imprimir()


class Navio(Maritimo):
    def __init__(self, nome, porte, num_cabines, num_carga):
        super().__init__(nome, porte)
        self.num_cabines = num_cabines
        self.num_carga = num_carga

    def imprimir(self):
        print(f'Numero de cabines: {self.num_cabines}')

    def mover(self):
        print(f'O navio está se movendo')

    def ancorar(self):
        print(f'O navio {self.nome} está ancorado')


