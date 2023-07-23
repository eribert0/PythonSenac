class Cliente:
    def __init__(self, nome, cpf, dataNasc):
        self.nome = nome
        self.cpf = cpf
        self.dataNasc = dataNasc

c1 = Cliente('Roger', '123456789-10', '09/03/2003')
print(c1.nome, c1.cpf, c1.dataNasc)