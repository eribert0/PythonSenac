class Cliente:
    def __init__(self, nome, cpf, data):
        self.nome = nome
        self.cpf = cpf
        self.dataNasc = data

    def __str__(self):
        return f'Nome: {self.nome} - CPF: {self.cpf}'


# Cliente teste
cliente1 = Cliente(nome='Roger Guedes', cpf='123456789-10', data='21/07/1995')
print(f'---------------------------------\n Nome: {cliente1.nome}\n---------------------------------\n CPF: {cliente1.cpf}\n---------------------------------\n Data de nascimento: {cliente1.dataNasc}\n---------------------------------\n')

