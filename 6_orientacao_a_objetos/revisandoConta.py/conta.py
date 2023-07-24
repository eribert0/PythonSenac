from cliente import Cliente

class Conta:
    def __init__(self, numConta, agencia, saldo):
        #self.titular = Cliente() 
        self.numConta = numConta
        self.agencia = agencia
        self.__saldo = saldo

    @property
    def saldo(self): #Saldo Get
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor): #Saldo Set
        self.__saldo = valor

conta_1 = Conta(numConta='12345-6', agencia='1234-5', saldo=5000)
print(f'Conta: {conta_1.numConta}\n--------------------------\nAgência: {conta_1.agencia}\n--------------------------\nSaldo em conta: {conta_1.saldo}\n--------------------------')
