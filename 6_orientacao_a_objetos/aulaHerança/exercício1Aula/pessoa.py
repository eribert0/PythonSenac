class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.salario = float

    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}\nCPF: {self.cpf}\nSalário: {self.salario}')
    
