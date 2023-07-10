dicioAluno = {}
for cont in range(1):
    dicioAluno['Nome'] = input('Digite o nome: ')
    dicioAluno['Media'] = float(input('Digite a media: '))
if dicioAluno['Media'] < 5:
    dicioAluno['Situação'] = 'Reprovado'
else:
    dicioAluno['Situação'] = 'Aprovado'
print(dicioAluno)