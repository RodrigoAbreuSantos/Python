lista = []
for c in range(5):
    peso = float(input('Digite o Peso: '))
    lista.append(peso)
print('O maior peso foi: {:.2f}kg e o menor peso foi: {:.2f}kg'.format(max(lista), min(lista)))