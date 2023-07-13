resposta = "nao";
contador = 1;

while resposta != "sim":
    resposta = input(f"Tentativa {contador}: Eu sou bonito? ");
    contador+=1;
    if contador == 10:
        break;

print("Obrigado por responder!");