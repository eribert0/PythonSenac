from cliente import Cliente

class Conta:
    
    def __init__(self, clienteNome, clienteCpf, clienteData, num, ag):
        self.cliente = Cliente(clienteNome, clienteCpf, clienteData) #parâmetro ou void
        self.numero = num
        self.agencia = ag
        self.__saldo = 0.0

    @property
    def getSaldo(self):
        return self.__saldo
    
    @getSaldo.setter
    def setSaldo(self, valorSaldo):
        self.__saldo = valorSaldo

    def __str__(self):
        return f'---------------------------------\n Cliente: {self.cliente.nome}\n---------------------------------\n CPF: {self.cliente.cpf}\n---------------------------------\n Data de nascimento: {self.cliente.dataNasc}\n---------------------------------\n'

"""
conta1 = Conta('Casimiro Miguel', '12345-6', '1234-5')
conta1.setSaldo = 250 #int(input('digite seu saldo: '))

print(f'Nome: {conta1.cliente}\n-----------------------\nConta: {conta1.numero}\n-----------------------\nAgência: {conta1.agencia}\n-----------------------\nSaldo: {conta1.getSaldo}\n')
"""