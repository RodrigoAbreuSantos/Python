dados = {'Nome': 'Pedro', 'Idade': 25}
print(dados['Nome'])
print(dados['Idade'])

dados['Sexo'] = 'M'# diferente do append em uma lista, para inserir dados no dicionario é so fazer isso
print(dados)

del dados['Idade']# vai excluir o indice idade
print(dados)

filme = {
    'titulo': 'Star Wars',
    'Ano': 1977,
    'Diretor': 'George Lucas'
}

print(filme.values())# vai retornar todos os valores do dicionario
print(filme.keys())# vai retornar as chaves do dicionario
print(filme.items())# vai retornar as chaves e os valores dentro das chaves

for chave, valor in filme.items():# Na lista seria enumerate, ja dicionario utiliza items()
    print(f'O {chave} é: {valor}')

locadora = [{
    'titulo': 'Star Wars',
    'Ano': 1977,
    'Diretor': 'George Lucas'
},
{
    'titulo': 'Avengers',
    'Ano': 2012,
    'Diretor': 'Joss Whedon'
},
{
    'titulo': 'Matriz',
    'Ano': 1999,
    'Diretor': 'Wachowski'
}
]

print(locadora[0]['Ano'])# como é uma lista com dicionarios dentro então o indice 0 é primeiro diconario
# da lista, e o ano seria o valor da chave
print(locadora[2]['titulo'])

pessoas = {'Nome': 'Rodrigo', 'Sexo': 'M', 'Idade': 18}
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')# se colocasse '' daria erro então é "" 

pessoas['Nome'] = 'Leandro'# voce pode mudar o valor de uma chave
pessoas['Peso'] = 98# voce pode acrescentar uma nova chave e um valor para ela

brasil = []
estado1 = {'Uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'Uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)# uma lista com dicionarios dentro

estado = {}
brasil = []

for cont in range(3):
    estado['Uf'] = input('Digite a Unidade Federativa: ')
    estado['Sigla'] = input('Digite a Sigla: ')
    brasil.append(estado.copy())
print(brasil)
for dicio in brasil:
    for valor in dicio.values():
        print(f'{valor}', end=' ')
    print()