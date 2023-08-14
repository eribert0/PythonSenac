"""
class bombaCombustivel: 
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        # a classe tem que ter no mínimo esses 3 atributos
        self.tipoCombustivel = tipoCombustivel # tipo de combustivel
        self.valorLitro = valorLitro  # Valor do litro 
        self.quantidadeCombustivel = quantidadeCombustivel #quantidade de combustível total na bomba

    def abastecer_por_valor(self, valor):  
        return f'o carro foi abastecido com: {valor / self.valorLitro}'

    def abastecer_por_litro(self, litros):
        return f'{litros * self.valorLitro}' 
    
    def alterar_valor(self, valorLitro):
        self.valorLitro = valorLitro

    def alterarCombustivel(self, tipoComb): #altera o tipo de combustivel
        self.tipoCombustivel = tipoComb
    
    def alterarQuantidadeCombustivel(self, quantidadeComb):
        self.quantidadeCombustivel = quantidadeComb

bc1 = bombaCombustivel()
"""
class bombaCombustivel:
    
    def __init__(self, valorLitro, tipoCombustivel, quantidadeCombustivel):
        self.valorLitro = valorLitro
        self.tipoCombustivel = tipoCombustivel
        self.quantidadeCombustivel = quantidadeCombustivel

    """
    def teste(self):
        print(f'Bomba com {self.quantidadeCombustivel} litros de combustível')
    """
    def abastecer_por_valor(self, valor):
        r = valor/self.valorLitro
        self.quantidadeCombustivel -= r
        print(f'O carro foi abastecido com: {r} litros')

    def abastecerPorLitro(self, litros):
        print(f'Valor total: {litros * self.valorLitro}')
        self.quantidadeCombustivel -= litros

    def alterarValor(self, newValue):
        self.valorLitro = newValue

    def alterarCombustivel(self, newType):
        self.tipoCombustivel = newType

    def alterarQuantidadeCombustivel(self, newQuantity):
        self.quantidadeCombustivel = newQuantity

#Testando objeto bomba
bomba = bombaCombustivel(valorLitro=5.60, tipoCombustivel='Gasolina', quantidadeCombustivel=100)
print(f'Combustível disponível na bomba: {bomba.quantidadeCombustivel} litros')
bomba.abastecer_por_valor(int(input('Digite valor do abastecimento: ')))
print(f'Combustível disponível na bomba: {bomba.quantidadeCombustivel} litros')
bomba.alterarValor(float(input('Digite o preço por litro do combustível: ')))
bomba.abastecer_por_valor(int(input('Digite valor do abastecimento: ')))
print(f'Combustível disponível na bomba: {bomba.quantidadeCombustivel} litros')
