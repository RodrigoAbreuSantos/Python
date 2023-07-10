contIdade = 0
somatorioIdade = 0
contMulher = 0
maiorIdade = 0
nomeVelho = ''
for c in range(4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    contIdade = contIdade + 1
    somatorioIdade = somatorioIdade + idade
    sexo = input('Digite seu sexo: ')
    if c == 1 and sexo == 'H':
        maiorIdade = idade
        nomeVelho = nome
    if sexo == 'H' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome
    if sexo == 'M' and idade < 20:
        contMulher = contMulher + 1
media = somatorioIdade/contIdade
print('A media da idade do grupo é: {} o nome do homem mais velho é: {} e a qtde de mulher < 20 anos é: {}'.format(media, nomeVelho, contMulher))


