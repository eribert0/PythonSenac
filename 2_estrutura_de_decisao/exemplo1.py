nota1 = float(input("numero 1: "));

nota2 = float(input("numero 1: "));

nota3 = float(input("numero 1: "));

media = (nota1 + nota2 + nota3)/3.0;

print(f"A média é igual a {media}");

aprovado = media >=6.0;
reprovado = media <=3.0;

if aprovado:
    print("Você está aprovado");
else:
    print("Você está reprovado");