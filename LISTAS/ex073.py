aluno = []
dados = []
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Nota: ')))
    dados.append(float(input('Nota: ')))
    aluno.append(dados[:])
    dados.clear()
    resp = input('Deseja Continuar? S/N ').upper()[0]
    if resp == 'N':
        break
print(aluno)
for boletim in aluno:
    media = (boletim[1] + boletim[2])/2
    print(f'Nome: {boletim[0]}. Media: {media} ')

while True:
    mostrar = int(input('Mostrar nota de qual Aluno? '))
    if mostrar <= len(aluno)-1:
        print(f'Suas notas foram: {boletim[1]} e {boletim[2]}')
    resp = input('Deseja Continuar? S/N ').upper()[0]
    if resp == 'N':
        break

            
