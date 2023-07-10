matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
somaPares = 0
somaTerceiraColuna = 0
maxi = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares.append(matriz[linha][coluna])
            somaPares = somaPares + matriz[linha][coluna]
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
for linha in range(0,3):
    somaTerceiraColuna = somaTerceiraColuna + matriz[linha][2]
for coluna in range(0,3):
    if coluna == 0:
        maxi = matriz[1][coluna]
    elif matriz[1][coluna] > maxi:
        maxi = matriz[1][coluna]
print(pares)
print(somaPares)
print(somaTerceiraColuna)
print(maxi)