def ficha(jogador = 'desconhecido', gol = 0):
    if gol > 1:
        return f'O jogador {jogador} fez {gol} gols no campeonato'
    else:
        if gol > - 1:
            return f'O jogador {jogador} fez {gol} gol no campeonato'

#Programa Principal
nomeJogador = input('Digite o Nome do Jogador: ')
golJogador = str(input('quantis gols ele fez? '))
if golJogador.isnumeric():
    golJogador = int(golJogador)
else:
    golJogador = 0
if nomeJogador.strip() == '':
    print(ficha(gol=golJogador))
else:
    print(ficha(nomeJogador, golJogador))