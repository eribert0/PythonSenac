from funcionario import Funcionario
#from gerente import Gerente

#Solicitando as informações ao usuário
nome = input('Nome: ')
cpf = input('CPF: ')
cargo = input('Cargo: ')

funcionario1 = Funcionario(nome, cpf, cargo)
funcionario1.salario = float(input('Digite o salário do funcionário: '))

funcionario1.mostrar_informacoes()
horas = float(input('Quantidade de horas extras: '))
funcionario1.calculo_horaExtra(horas)

funcionario1.informacoes_funcionario()