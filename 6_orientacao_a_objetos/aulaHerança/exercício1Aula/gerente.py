from pessoa import Pessoa

class Gerente(Pessoa):
    def __init__(self, nome, cpf, setor):
        super().__init__(nome, cpf)
        self.setor = setor
        self.qtdEquipe = int

    def informacoes_Gerente(self):
        super().mostrar_informacoes(self)
        print(f'Setor: {self.setor}\nQuantidade da equipe: {self.qtdEquipe}\n')
    
    def informacoes_bonificacao(self):
        if self.qtdEquipe >= 10:
            return self.salario + (self.salario * 0.1)
        else:
            return self.salario + (self.salario * 0.05)