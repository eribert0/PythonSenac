"""
try:
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite um numero: '))
    div = num1/num2
    print(div)
except ValueError as e:
    print('Error! Digite um numero válido!')
except ZeroDivisionError as e2:
    print('Error! Divisão por zero!')
else:
    print('Continua 1')
finally:
    print('Continua 2')

"""
class ExcecaoError(Exception):
    def __init__(self, message):
        super().__init__(message)

def divisao(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError('Error! Divisão por zero!')
    else:
        return n1/n2

try:    
    resultado = divisao(int(input('Valor 1:')), int(input('Valor 2:')))
    print(f'Resultado da divisão: {resultado}')
except ZeroDivisionError as e:
    print(e)
    #raise ValueError('Valor inesperado') from e