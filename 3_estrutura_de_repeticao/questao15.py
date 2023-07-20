num1 = 1
num2 = 1
aux = 0

n = int(input('digite o n-ésimo termo: '))

while num1 <= n:
    print(num1, end=' ')
    aux = num1+num2
    num1 = num2
    num2 = aux