from classe_a import ClasseA
from classe_b import ClasseB
from classe_c import ClasseC

class Main:
    def __init__(self):
        self.classe_a_obj = ClasseA(atributo_a='Valor do Atributo A')
        self.classe_b_obj = ClasseB(atributo_b='Valor do Atributo B')
        self.classe_c_obj = ClasseC(atributo_c='Valor do Atributo C')

    def main_method(self):
        print('Chamando métodos das classes:')
        print(self.classe_a_obj.metodo_a())
        print(self.classe_b_obj.metodo_b())
        print(self.classe_c_obj.metodo_c())

main_obj = Main()
main_obj.main_method()