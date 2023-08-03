from boneca import Boneca
from car import Car

carro1 = Car()
carro1.faixaE = 'A partir de 3 anos'
carro1.controle = True
carro1.marca = 'Hot Wheels'
carro1.preco = 150.90
carro1.tipo = 'Jipe'

print(carro1)
carro1.imprimir()
carro1.ligar()
carro1.desligar()

boneca = Boneca()
boneca.nome = 'Barbie'
boneca.faixaE = 'A partir de 4 anos'
boneca.tipo = 'Mini boneca'
boneca.tamanho = 10
print(boneca)
