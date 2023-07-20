peso_limite = 50.0

peso_peixes = float(input('Digite \
o peso dos peixes: '))

multa = 0.0

if peso_peixes > peso_limite:
    excesso = peso_peixes - peso_limite
    multa = excesso * 4

print(f'O valor de multa é \
R$ {multa} ')