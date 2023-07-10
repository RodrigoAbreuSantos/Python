cadastro = {}
lista = []
contPessoa = soma = media = 0
while True:
    cadastro['Nome'] = input('Nome: ')
    cadastro['Sexo'] = input('Sexo: M/F ').upper()[0]
    cadastro['Idade'] = int(input('Idade: '))
    soma = soma + cadastro['Idade']
    contPessoa += 1
    lista.append(cadastro.copy())
    resp = input('Deseja Continuar? S/N ').upper()[0]
    if resp == 'N':
        break
media = soma/contPessoa
print('-=-'*30)
print(f'Ao todo foram cadastrados {contPessoa} pessoas')
print(f'A media das idades é: {media}')
print('As mulheres cadastradas foram: ', end='')
for a in lista:
    if a['Sexo'] == 'F':
        print(f'{a["Nome"]}',end=', ')
    if a['Idade'] > media:
        print(f'\n nome = {a["Nome"]}; sexo = {a["Sexo"]}; idade = {a["Idade"]}')