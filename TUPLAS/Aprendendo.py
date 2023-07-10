lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for comida in lanche:
    if comida == 'Suco':
        print(f'Eu vou tomar {comida}')
    else:
        print(f'Eu vou comer {comida}')
print('\n')

for cont in range(0, len(lanche)):
    print(f'O cardapio {cont+1} é ==> {lanche[cont]}')
print('\n')

for pos, comida in enumerate(lanche):
    print(f'O cardapio {pos+1} é ==> {comida} ')

print(sorted(lanche))

a = (1,2,3,6)
b = (4,5,6)
c = a+b
d = b+a
print(c,'\n',d)
print(d.count(5)) # quantas vezes apareceu
print(d.index(5)) # Posição em que apareceu
print(d.index(6,3)) # a posição do 6 a partir do indice 3

pessoa = ('Rodrigo', 18, 'M', 62.00)
print(pessoa)
del(pessoa) # você pode excluit uma tupla inteira, mas não pode excluir apenas um elemento dela