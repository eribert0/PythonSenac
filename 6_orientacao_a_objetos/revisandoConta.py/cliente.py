class Cliente:
    def __init__(self, nome, snome, cpf, dataNasc):
        self.nome = nome
        self.sobrenome = snome
        self.cpf = cpf
        self.dataNasc = dataNasc

c1 = Cliente('Eriberto', 'Junior', '123456789-10', '05/03/2000')
print(f'Nome: {c1.nome}\n--------------------------\nSobrenome: {c1.sobrenome}\n--------------------------\nCPF: {c1.cpf}\n--------------------------\nNascimento: {c1.dataNasc}\n--------------------------')