num1 = int(input("numero 1: "));

num2 = int(input("numero 2: "));

num3 = int(input("numero 3: "));

maior = 0;

if num1 > num2 and num1>num3:
    maior = num1;
elif num2 > num1 and num2>num3:
    maior = num2;
else:
    maior = num3;
print(f"O maior número é o {maior}");