from funcionario import Funcionario
from gerente import Gerente

#Solicitando as informações ao usuário
#nome = input('Nome: ')
#cpf = input('CPF: ')
#cargo = input('Cargo: ')

#f = Funcionario(nome, cpf, cargo)
#f.salario = float(input('Digite o salário do funcionário: '))
#f.mostrar_informacoes()
"""
horas = float(input('Quantidade de horas extras: '))
f.calculo_horaExtra(horas)
f.informacoes_funcionario()
"""

nome_ger = input('Nome: ')
cpf_ger = input('CPF:')
setor_ger = input('Setor: ')

g = Gerente(nome_ger, cpf_ger, setor_ger)
g.qtdEquipe = int(input('Quantidade da equipe:'))
g.informacoes_Gerente()
