from random import shuffle
lista = []
for x in range(4):
    nome = input("Digite o nome: ").upper()
    lista.append(nome)
    shuffle(lista) #pegaram os nvalores dentro da lista e colocora em ordem aleatoria
print('A ordem de apresentação sera: {}'.format(lista))