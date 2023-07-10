from random import randint
from time import sleep
sorteio = []
pergunta = int(input('Quantos jogos você quer que sorteio? '))
for jogo in range(0, pergunta):
    aleatorio = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    aleatorio.sort()
    print(aleatorio)
    sleep(1.5)
print('BOA SORTE')




from random import randint
from time import sleep
tot = 0
pergunta = int(input('Quantos jogos você quer que sorteio? '))
while tot <= pergunta:
    cont = 0
    lista = []
    jogos = []
    while True:
        num = int(randint(1,60))
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(2)