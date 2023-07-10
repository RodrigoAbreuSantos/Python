from random import randint
computador = randint(0,10)
num = 11
cont = 0
while computador != num:
    cont = cont + 1
    print('{} Tentativa'.format(cont))
    num = int(input('Digite um numero entre 0 a 10: '))
    if computador > num:
        print('Digite um numero maior')
    else:
        print('Digite um numero menor')
print('O computador escolheu {} e o tanto de palpites foi {}'.format(computador, cont))