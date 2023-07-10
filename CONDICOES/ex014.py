from time import sleep
from random import randint
x = randint(0,5)
numUsuario = int(input('Tente advinhar o numero de 0 a 5 escrito pelo computador: '))
print("Processando....")
sleep(3)
print('Parabens você acertou' if numUsuario == x else 'Infelizmente você errou')
print('O numero escolhido pelo computador foi: {}'.format(x))


