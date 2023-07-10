cont = totGasto = contMenor = 0
lista = lista2 = []
while True:
    nome = input('Digite o nome do Produto: ')
    preco = float(input('Digite o Preço do Produto: '))
    totGasto = totGasto + preco
    contMenor += 1
    lista.append(nome)
    lista2.append(preco)
    if preco > 1000:
        cont += 1
    if contMenor == 1:
        menor = preco
        nomeBarato = nome
    else:
        if menor > preco:
            menor = preco
            nomeBarato = nome
    resp = input('Deseja Continuar S/N? ').upper()[0]
    if resp not in 'SN':
        print('Apenas S ou N')
    if resp == 'N':
        break
print(f'O total de gasto foi {totGasto}, a qtde de prod acima de 100R$ é: {cont} e o prod mais barato é: {menor} e seu nome é: {nomeBarato}')