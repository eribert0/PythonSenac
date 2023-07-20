lado1 = int(input('Digite o lado 1: '))
lado2 = int(input('Digite o lado 2: '))
lado3 = int(input('Digite o lado 3: '))

if lado1 < lado2 + lado3 or lado2 < lado1 + lado3 or lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print('Triângulo Equilátero')
    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')

else:
    print('Não forma Triangulo')