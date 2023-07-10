valores = []
for valor in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
for posicao, valor in enumerate(valores):
    if valor == max(valores):
        print(f'Posição: {posicao} ==> Valor: {max(valores)}')
    if valor == min(valores):
        print(f'Posição: {posicao} ==> Valor: {min(valores)}')
