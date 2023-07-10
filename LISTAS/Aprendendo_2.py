dados = ['Pedro', 25] # uma lista normal
pessoas = []
pessoas.append(dados[:]) # uma lista que vai ter outra lista
print(pessoas)

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]] # uma lista com 3 listas dentro
print(pessoas)
print(pessoas[0]) # o indice zero na lista ou seja seria ['Pedro', 25]
print(pessoas[0][0]) # o iten 0 do indice zero na lista ou seja, o indice zero seria ['Pedro', 25].
# e o iten zero seria Pedro

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
for p in galera: # para cada indice nessa lista
    print(p) # vai printar cada indice 
for p in galera:    
    print(p[0]) # vai printar apenas o primeiro elemento de cada indice

galera = []
dado = []
for c in range(3): 
    dado.append(input('Nome: ')) # dado vai receber uma string nome
    dado.append(int(input('Idade: '))) # dado vai receber uma idade
    galera.append(dado[:]) # vai adicionar uma copia de dados em galera
    dado.clear() # a cada repetição vai excluir o dado, pois ja vai estar em galera e se não excluir vai ser duplicado na proxima repetição
print(galera)
for p in galera:
    if p[1] > 21:
        print(p[0])