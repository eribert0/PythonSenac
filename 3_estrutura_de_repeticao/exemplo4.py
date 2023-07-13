maior = float("-inf")

for item in range(5):
    numero = float(input(f"Digite o numero {item + 1}:"));
    if numero > maior:
        maior = numero;

print(f"O maior numero digitado foi o {maior}.");