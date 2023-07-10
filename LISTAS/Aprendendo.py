lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
lanche[3] = 'Picole' # vai trocar o pudim por picole
print(lanche)
lanche.append('Pudim') # vai adicionar pudim na ultima posição da lista
print(lanche)
lanche.insert(0,'Cachoro Quente') # vai adicionar na posiçã solicitada 
print(lanche)
del lanche[3] # vai apagar o elemento na posição 3
print(lanche)
lanche.pop(3) # vai apagar o elemento na posição 3
if 'Pizza' in lanche:
    lanche.remove('Pizza') # vai apagar pelo valor, não pelo indice
    # remove elimina apenas o primeiro valor que achou. Se tivesse 2 pizzas ele removeria apenas a 1

valores = list(range(4,11)) # vai criar uma lista com os valores de 4 até 10
print(valores)

valores = [8,9,3,4,7]
valores.sort() # vai colocar a lista em ordem crescente
print(valores)
valores.sort(reverse=True) # vai colocar a lista em ordem decrescente
print(valores)

print(len(valores)) # vai dizer quantos elementos existme na lista

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores): # o enumerate pega a chave e o valor da variavel 
    print(f'Os valores são: {v}, e está na posição {c}')

valores = list() # list() é um comando para dizer que é uma lista

for valor in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print(valores)



a = [2,3,4,7]
b = a # quando você diz que uma lista é igual a outra, você ta fazendo uma ligação entre elas, e não apenas copiando
print(f'A: {a}')
print(f'B: {b}')

b[2] = 8 
print(f'A: {a}')
print(f'B: {b}')

a = [2,3,4,7]
b = a[:] # Você esta dizendo que b vai receber todos os valores de a, 
# fazendo isso você está apenas copiando a lista e não interligando
print(f'A: {a}')
print(f'B: {b}')

b[2] = 8 
print(f'A: {a}')
print(f'B: {b}')