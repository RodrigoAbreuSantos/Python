jogador = {}
lista = []
jogador['Nome'] = input('Digite o nome do Jogador: ')
partida = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
for cont in range(0, partida):
    jogador['Gols'] = int(input(f'Quantos gols na Partida {cont}? '))
    lista.append(jogador['Gols'])
jogador['Gols'] = lista
jogador['Total'] = sum(lista)
print('-=-'*30)
print(f'O jogador {jogador["Nome"]} jogou {partida} partidas')
cont2 = 0
for gols in jogador['Gols']:
    cont2 += 1
    print(f'   ==> Na partida {cont2-1} fez {gols}')
print(f'Foi um total de {jogador["Total"]} gols')
print(jogador)