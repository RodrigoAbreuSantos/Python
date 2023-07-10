pessoa = []
dados = []
cont = maiorPeso = menorPeso = 0
while True:
    cont = cont + 1
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    if len(pessoa) == 0:
        maiorPeso = dados[1]
        menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    pessoa.append(dados[:])
    dados.clear()
    resp = input('Deseja Continuar? S/N ').upper()[0]
    if resp == 'N':
        break
for nomePeso in pessoa:
    if nomePeso[1] == maiorPeso:
        nomeMaiorPeso = nomePeso[0]
    if nomePeso[1] == menorPeso:
        nomeMenorPeso = nomePeso[0]
print(f'O total de pessoas é: {cont}, o maior peso é {maiorPeso}. Peso de {nomeMaiorPeso} e o menor é {menorPeso}. Peso de {nomeMenorPeso}')


''' Resolução do Exercicio: Primeiramente você cria uma lista temporaria que a cada laço vai limpar essa lista
e vai adicionar na lista pessoa. Mas antes de limpar e adicionar, você verifica se o tamanho da lista é 0, 
pois o tamanho 0 é o primeiro dado dessa lista com isso você coloca que o maior e menor pesso vai receber
o peso do primeiro dado. Feito isso na proxima repetição o len não vai ser 0, vai etar no segundo dado 
então vai ser 1, com isso você faz um else. Assim dentro desse else você verifica o maior e o menor peso
se o dado[1] que é o dado desse laço que etsá agora, for maior que o maiorPeso que é o peso do indice 0
o maiorPeso vai virar o dado[1]. Ai vai fazer isso a cada laço e vai trocando se o dado do laço que está agora
for maior que o maiorPeso atual. Faz a mesma coisa para o menor peso. Se o o dado[1] que é o dado atual,
for menor que o menor peso o menorPeso vira dado[1]. Feito isso agora você faz um for 
para verificar cada lista de nome e Peso dentro da lista pessoa. se o nomeePeso[1] que é o pesoa da pessoa
for igual ao maiorPeso você cria uma variavel nomeMaiorPeso que vai receber o nomePeso[0] que é
o nome da pessoa se o nomePeso[1] == ao menorPeso faz a mesma coisa
'''