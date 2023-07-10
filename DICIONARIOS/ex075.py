from random import randint
from time import sleep
dado = {'Jogador1': randint(1,6), 'Jogador2': randint(1,6), 'Jogador3': randint(1,6), 'Jogador4': randint(1,6)}
print('Valores Sorteados: ')
for chave, valor in dado.items():
    print(f'O {chave} tirou {valor} no dado')
    sleep(1.5)
print('-=-'*30)
print('                  == Rankins dos Jogadores ==')
cont = 0
for ordenar in sorted(dado, key= dado.get, reverse=True):
    cont = cont + 1
    print(f'{cont}º: {ordenar} com {dado[ordenar]}.')
    sleep(1.5)