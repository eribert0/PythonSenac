# Hard coder é alog que foi escrito diretamente no código
class Carro:
    def __init__(self, nome):
        self.nome = nome
        
    def acalerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acalerar()
# fusca.nome = 'Fusca'

celta = Carro('Celta')
# celta.nome = 'Celta'
print(celta.nome)
celta.acalerar()