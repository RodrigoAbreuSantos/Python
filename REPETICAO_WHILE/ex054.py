cont = contM = contF = 0
while True:
    idade = int(input('Digite a Idade: '))
    sexo = input('Digite o Sexo F/M: ').upper()[0]
    if idade > 18:
        cont += 1
    if sexo == 'M':
        contM += 1
    if idade < 20 and sexo == 'F':
        contF += 1
    resp = input('Deseja Continuar S/N? ').upper()[0]
    if resp not in 'SN':
        print('Apenas S ou N')
    if resp == 'N':
        break
print(f'O total de pessoas com mais de 18 anos são: {cont}, o total de homens cadastrados são: {contM} e o total de mulheres com menos de 20 anos  são: {contF}')