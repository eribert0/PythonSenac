nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2) / 2.0

conceito_A = media >= 9 and media <= 10.0
conceito_B = media >= 7.5 and media < 9.0
conceito_C = media >= 6.0 and media < 7.5
conceito_D = media >= 4.0 and media < 6.5
conceito_E = media >= 0.0 and media < 4.0

if conceito_A or conceito_B or conceito_C or conceito_D:
    print('Aprovado')
elif conceito_D or conceito_E:
    print('Reprovado')
else:
    print('Algum erro aconteceu')
    