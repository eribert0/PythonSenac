class Cliente:
    def __init__(self, nome, cpf, dataNasc):
        self.nome = nome
        self.cpf = cpf
        self.dataNasc = dataNasc

c1 = Cliente('Roger', '123456789-10', '09/03/2003')
print(f'Nome: {c1.nome}'\nCPF:{c1.cpf}\nNascimento: {c1.dataNasc})
