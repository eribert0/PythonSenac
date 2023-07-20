num1 = 0
num2 = 1
aux = 0

while num1 <= 500:
    print(num1, end=' ')
    aux = num1 + num2
    num1 = num2
    num2 = aux

