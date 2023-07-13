# lista_num = [10];

lista_num = [];
lista_par = [];
lista_impar = [];

for i in range(20):
    numero = int(input(f"Digite o {i + 1}° numero: "));
    lista_num.append(numero);

print(f"Lista de números: {lista_num}")

for i in lista_num:
    if i%2==0:
        lista_par.append(i);

print(f"Lista de números Pares: {lista_par}")

for i in lista_num:
    if i%2!=0:
        lista_impar.append(i);

print(f"Lista de números Ímpares: {lista_impar}")