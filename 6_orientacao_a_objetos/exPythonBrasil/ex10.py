class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
    self.tipoCombustivel = tipoCombustivel # tipo de combustivel
    self.valorLitro = valorLitro  # Valor do litro 
    self.quantidadeCombustivel = quantidadeCombustivel #quantidade de combustível total na bomba

    def abastecer_por_valor(self, valor):  
        return f'{valor / self.valorLitro} '

    def abastecer_por_litro(self, quantidadeLitros):
        return quantidadeLitros / 
    
    def alterar_valor(self, valorLitro):
        self.valorLitro = valorLitro

    def alterarCombustivel(self, tipoComb): #altera o tipo de combustivel
        self.tipoCombustivel = tipoComb
    
    def alterarQuantidadeCombustivel(self, quantidadeComb):
        self.quantidadeCombustivel = quantidadeComb

bc1 = bombaCombustivel()
