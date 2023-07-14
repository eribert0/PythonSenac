def soma(numeros):
    #cria a variavel total e atribui
    # o valor 0
    total = 0
    #laço para somar os numeros da lista
    for numero in numeros:
        total = total + numero
    # retornando o total
    return total

#definindo a função maior
def maior(numeros):
    #cria a variável maior e atribui
    #o primeiro valor da lista 
    maior = numeros[0]
    # laço para percorrer a lista
    # de números
    for numero in numeros:
        #verificando se o numero
        #é maior que o maior
        if numero > maior:
            #atribuindo o novo maior
            maior = numero
    #retornando o maior
    return maior
def is_list(numeros):
    if type(numeros) == list:
        return type(numeros) == list
    
###################################
lista1 = [2, 14, 11]
lista2 = [2, 14, 11, 'jose', 6, 7, 8, 9, 10]

print(f"Resultado 1: {soma(lista1)}")
print(f"Resultado 2: {soma(lista2)}")

print(f"Maior 1: {maior(lista1)}")
print(f"Maior 2: {maior(lista2)}")
