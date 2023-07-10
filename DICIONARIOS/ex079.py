jogador = {}
lista = []
jogadores = []
while True:
    jogador['Nome'] = input('Digite o nome do Jogador: ')
    partida = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
    for cont in range(0, partida):
        jogador['Gols'] = int(input(f'Quantos gols na Partida {cont}? '))
        lista.append(jogador['Gols'])
    jogador['Gols'] = lista.copy()
    jogador['Total'] = sum(lista)
    lista.clear()
    jogadores.append(jogador.copy())
    resp = input('Deseja Continuar? S/N ').upper()[0]
    if resp == 'N':
        break
print('-=-'*30)
print(f'{jogadores}\n')
print('cod nome       gols      total')
print('-'*30)
for chave, valor in enumerate(jogadores):
    print(f'{chave}   {valor["Nome"]}      {valor["Gols"]}      {valor["Total"]}')
