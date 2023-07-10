from random import randint
from time import sleep
def sortear(lista):
    print(f'Sorteando 5 valores da lista: ',end='')
    for valor in lista:
        print(f'{valor}', end=' ')
        sleep(0.5)
    print('')
    
#Programa Principal
valores = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
sortear(valores)

def somaPar(lista):
    somaPares = 0
    for valor in lista:
        if valor % 2 == 0:
            somaPares = somaPares + valor
    print(f'Somando os valores pares de: {lista}, temos: {somaPares}')
    

#Programa Principal
somaPar(valores)