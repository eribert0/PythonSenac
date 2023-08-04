from pessoa import Pessoa

class Gerente:
    def __init__(self, nome, cpf, setor):
        self.nome = nome
        self.cpf = cpf
        self.setor = setor
        self.qtdEquipe = int

    def informacoes_Gerente(self):
        print(f'Nome: {self.nome}\nCPF: {self.cpf}\nSetor: {self.setor}\n')
    
    def informacoes_bonificacao(self):
        if self.qtdEquipe >= 10:
            salario += salario*0.95
        else:
            salario += salario*0.95