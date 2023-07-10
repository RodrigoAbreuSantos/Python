from random import randint
cont = 0
while True:
    computador = randint(0,10)
    jogador = int(input('Jogo Par/Impar. Digite um numero: '))
    escolha = input('Par ou Impar: ').upper()
    soma = jogador + computador
    if soma % 2 == 0 and escolha == 'PAR':
        cont = cont + 1
    else:
        break
print(f'Você ganhou {cont} vezes')