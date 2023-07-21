from cliente import Cliente
from conta import Conta

c1 = Cliente('Camila', '123456789-10', '23/04/2002')
print(c1)

conta = Conta(c1.nome, c1.cpf, c1.dataNasc, '1234-5', '12345-6')
print(f'Conta: {conta.cliente.nome}')