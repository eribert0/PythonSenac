from armazenamento import Armazenamento
from memoria import Memoria
from processador import Processador

class Main:
    def __init__(self, armazenamento_obj, memoria_obj, processador_obj):
        self.armazenamento_obj = armazenamento_obj
        self.memoria_obj = memoria_obj
        self.processador_obj = processador_obj

    def metodo_main(self):
        print('Especificações:\n ')
        print(self.armazenamento_obj.metodo_arm())
        print('-----------------------------------')
        print(self.memoria_obj.metodo_mem())
        print('-----------------------------------')
        print(self.processador_obj.metodo_pro())
        print('-----------------------------------\n')
        

computador1 = Main(Armazenamento(tipo='SSD', capacidade=480), Memoria(marca='HyperX', capacidade=8), Processador(modelo='Intel i3', velocidade='3.40'))
computador1.metodo_main()

computador2 = Main(Armazenamento(tipo='HD', capacidade=1000), Memoria(marca='Juhor', capacidade=16), Processador(modelo='AMD Ryzen 5', velocidade='3.90'))
computador2.metodo_main()
