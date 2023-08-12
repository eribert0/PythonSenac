class Cliente:
    def __init__(self, nome, snome, cpf, dataNasc):
        self.nome = nome
        self.sobrenome = snome
        self.cpf = cpf
        self.dataNasc = dataNasc

    def dados_cliente(self): 
        return f'Nome: {self.nome}\n-----------------------------\nSobrenome: {self.sobrenome}\n-----------------------------\nCPF: {self.cpf}\n-----------------------------\nNascimento: {self.dataNasc}\n-----------------------------'


"""
#cliente teste
c1 = Cliente('Roger', 'Guedes', '123456789-10', '12/07/2001')
print(f'Nome: {c1.nome}\n--------------------------\nSobrenome: {c1.sobrenome}\n--------------------------\nCPF: {c1.cpf}\n--------------------------\nNascimento: {c1.dataNasc}\n--------------------------')
"""
