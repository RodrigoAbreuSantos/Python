lista = []
for i in range(3):
    n = float(input('Digite um numero: '))
    lista.append(n)
if lista[0] < lista[1] and lista[0] < lista[2]:
    if lista[1] < lista[2]:
        menor = lista[0]
        maior = lista[2]
if lista[1] < lista[0] and lista[1] < lista[2]:
    if lista[0] > lista[2]:
        menor = lista[1]
        maior = lista[0]
if lista[2] < lista[1] and lista[2] < lista[0]:
    if lista[0] < lista[1]:
        menor = lista[2]
        maior = lista[1]
print('O menor numero é: {} e o maior numero é: {}'.format(menor,maior))
