from math import factorial
from time import sleep
while True:
    num = int(input('Digite um numero: '))
    print('Seu Fatorial é: {}'.format(factorial(num)))
    resp = input('Deseja Continuar? S/N ').upper()
    if resp == 'N':
        for i in range(num, 0, -1):
            print(i)
            sleep(1)
        break

print('FIM')