#tabuada 
num = 0;
while num < 1 or num > 10:
    num = int(input("Digite um numero: ")); 

print(f"Tabuada de {num}: ")
for i in range(1, 11):
    resultado = num * i;
    print(f"{num} * {i} = {resultado}")