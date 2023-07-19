#Calculador com while

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operacao = input('Digite a operação desejada: ')

    numeros_valido = None
    numero_1_float = 0
    numero_2_float = 0
    
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos == None:
        print('Um ou ambos os numeros são invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operacao not in operadores_permitidos:
        print('Operador invalido.')
        continue

    if len(operacao) > 1:
        print('Digite apenas um operador!')
        continue
    
    if operacao == '+':
        print(f'{numero_1_float} + {numero_2_float} = ', numero_1_float + numero_2_float)
    elif operacao == '-':
        print(f'{numero_1_float} - {numero_2_float} = ', numero_1_float - numero_2_float)
    elif operacao == '*':
        print(f'{numero_1_float} * {numero_2_float} = ', numero_1_float * numero_2_float)
    elif operacao == '/':
        print(f'{numero_1_float} / {numero_2_float} = ', numero_1_float / numero_2_float)
    else:
        print('Nunca deveris chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair:
        break