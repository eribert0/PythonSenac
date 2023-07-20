from pessoaClass import Pessoa

p2 = Pessoa('Joao', 'Soares')
#p2.nome = 'José'
#p2.sobrenome = 'Tavares'
p2.peso = 80.1
p2.altura = 190.7
# p2.imprimir()

p2.alterar_peso = 75.7
p2.falar()
p2.andar()
print(f'IMC: {p2.calculoIMC(p2.peso, p2.altura)}')
p2.imprimir()
#print(p2)
