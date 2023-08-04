from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf)
        self.cargo = cargo

    def informacoes_funcionario(self):
        super().mostrar_informacoes()
        print(f'Cargo: {self.cargo}\n')

    def calculo_horaExtra(self, qtdHoras):
        self.salario += qtdHoras * 15.00
        return self.salario