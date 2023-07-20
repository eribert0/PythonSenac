valor_hora = float(input('Digite o valor ganho \
por horas: '))
horas = float(input('Digite a quantidade \
de horas trabalhadas no mês: '))
print('')

iprf = 0.11
inss = 0.08
sindicato = 0.05
salario_bruto = valor_hora * horas

print(f'Salário bruto: R$ {salario_bruto}')
r1=salario_bruto*iprf
print(f'Valor pago ao IPRF: R$ {r1}')
r2 = salario_bruto * inss
print(f'Valor pago ao INSS: R$ {r2}')
r3 = salario_bruto * sindicato
print(f'Valor pago ao Sindicato: R$ {r3}')
salario_liquido = salario_bruto - (r1+r2+r3)
print(f'Salário líquido: R$ {salario_liquido}')

