from math import hypot

catO = float(input('Digite o cateto oposto: '))
catA = float(input('Digite o cateto Adjacente: '))

print('A hipotenusa de {} e de {} é {:.2f}: '.format(catO, catA, hypot(catO, catA)))
