contador = 1;
maior = 0;

while contador <=5:
    numero = int(input(f"Digite o {contador}° numero: "));
    if contador == 1 or numero > maior:
        maior = numero;
    contador +=1;

print(f"O maior valor dos 5 numeros é {maior}!!");