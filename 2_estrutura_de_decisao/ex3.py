nome = input('Digite o primeiro nome: ')
tamanho_nome = len(nome)
if nome:
    if tamanho_nome >=1 and <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    elif tamanho_nome > 6:
        print('Seu nome é grande')
else:
    print('Você não digitou nada')