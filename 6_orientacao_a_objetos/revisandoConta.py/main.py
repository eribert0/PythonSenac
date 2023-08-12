from cliente import Cliente
from conta import Conta

#Criando objeto da classe cliente
cliente1 = Cliente(nome='João', snome='Silva', cpf='123456789-12', dataNasc='01/01/1990')

#Criando objeto da classe conta
conta1 = Conta(numConta='12345-6', agencia='1234-5', saldo=4000)

#associando a conta ao cliente
cliente1.conta = conta1

#adicionando o método que retorna as informações concatenadas
def dados_cliente_conta(self):
    return f'{self.dados_cliente()}\n{self.conta.dados_conta()}'

#adicionando o método à classe cliente
Cliente.dados_cliente_conta = dados_cliente_conta

print(cliente1.dados_cliente_conta())
################################
#          Cliente 2           #
################################
cliente2 = Cliente(nome='Roger', snome='Guedes', cpf='123456789-13', dataNasc='19/11/1989')
conta2 = Conta(numConta='23456-7', agencia='2345-6', saldo = 2500)

cliente2.conta = conta2

print(cliente2.dados_cliente_conta())