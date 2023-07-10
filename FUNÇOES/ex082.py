from time import sleep
def contagem(inico, fim, passo):
    print('\n')
    print('-=-'*20)
    for cont in range(inico, fim, passo):
        print(cont, end=' ')
        sleep(0.5)
    print('\n')

#Programa Principal
contagem(1, 11, 1)
contagem(10, -1, -2)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)