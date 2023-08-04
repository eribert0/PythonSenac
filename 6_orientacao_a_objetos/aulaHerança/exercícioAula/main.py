from retangulo import Retangulo
from circulo import Circulo

retangulo = Retangulo()
retangulo.finalidade = 'peça'


retangulo.base = int(input('Digite o valor da base: '))
retangulo.altura = int(input('Digite o valor da altura: '))

retangulo.areaRetangulo()

circulo = Circulo(int(input('Digite o valor do raio:')))

circulo.area_circulo()
