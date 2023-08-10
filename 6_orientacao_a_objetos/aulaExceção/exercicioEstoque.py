########### Corrigir bug do numero negativo #####################

class EstoqueNegativoError(Exception):
    def __init__(self, message):
        super().__init__(message)
    
class EstoqueInsuficienteError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Produto:
    
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def aumentar(self, quantidade):
        if quantidade >=0:
            self.quantidade += quantidade
        else:
            raise EstoqueNegativoError('Quantidade de aumento não pode ser negativa ou nula')

    def diminuir(self, quantidade):
        if quantidade >=0:
            if self.quantidade >= quantidade:
                self.quantidade -= quantidade
            else:
                raise EstoqueInsuficienteError('Quantidade de estoque inferior')
        else:
            raise EstoqueNegativoError('Quantidade de diminuição não pode ser negativa')

#Teste
try:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Preco do produto: '))
    quantidade = int(input('Quantidade do produto: '))
    
    produto1 = Produto(nome, preco, quantidade) #nome='bola', preco=20.00, quantidade=5)

    num = input('Digite [+] para adicionar produto(s) ou [-] para retirar produto(s):\n')
    if num == '+':
        produto1.aumentar(int(input('Diga quantos produtos você quer adicionar no estoque: ')))
    elif num == '-':
        produto1.diminuir(int(input('Diga quantos produtos você quer retirar no estoque: ')))
    else: 
        print('Dígito Inválido!')
    
    print(f'Nome do produto: {produto1.nome}\nPreço: R$ {produto1.preco}\nQuantidade: {produto1.quantidade}')

except ValueError:
    print(f'Error: Valor inválido inserido.')
