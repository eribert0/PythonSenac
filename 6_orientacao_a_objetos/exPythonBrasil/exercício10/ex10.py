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
