valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores: # se o numero não estiver dentro da lista valores você coloca ele dentro da lista
        valores.append(num)
        print('Valor Inserido com sucesso')
    else:
        print('Valor Duplicado....')
    resp = input('Deseja Continuar? S/N ').upper()[0]
    if resp == 'N':
        break
valores.sort()
print(valores)