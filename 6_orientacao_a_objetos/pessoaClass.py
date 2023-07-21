class Pessoa:
    # atributos da classe
    # nome = ''
    # sobrenome = ''
    peso = 0.0 #__atributo == private | _atributo = public yet 
    __altura = 0.0
    
    def __init__(self, n, snome):
        self.nome = n
        self.__sobrenome = snome

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def sobrenome(self):
        return self.__sobrenome
    
    @sobrenome.setter
    def sobrenome(self, snome):
        self.__sobrenome = snome

    ######################
    # métodos da classe
    ######################

    def andar(self):
        print('A pessoa está andando')

    def falar(self):
        print('A pessoa está falando')
    
    # calcula IMC
    def calculoIMC(self, altura, peso):
        return peso / altura ** 2
    
    # altera peso
    def alterar_peso(self, peso):
        self.peso = peso
    
    # retorna peso
    def  pegar_peso(self):
        return self.peso
    
    # método imprimir (lembra to String)
    def imprimir(self):
        print(f'Nome: {self.nome}\nSobrenome: {self.sobrenome}\nPeso: {self.peso}\nAltura: {self.altura}')
    
    def __str__(self):
        return f'Nome: {self.nome}\nSobrenome: {self.sobrenome}\nPeso: {self.peso}\nAltura: {self.altura}'

if __name__ == '__main__':

    p1 = Pessoa('José', 'Santos')
    p1.imprimir()
    p1.nome = 'Maria'
    p1.sobrenome = 'Silva'
    p1.imprimir()
    #p1.peso = 50.20
    # p1.altura = 180.10

    """
    p1.alterar_peso(60.7)
    p1.falar()
    p1.andar()
    print(f'IMC: {p1.calculoIMC(p1.peso, p1.altura)}')
    p1.imprimir()
    print(p1)
    """