primeiroTermo = int(input('Digite o Primeiro Termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiroTermo
cont = 1
mais = 10
tot = 0
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        cont += 1
        print('{} ==> '.format(termo), end= '')
        termo = termo + razao
    mais = int(input('\nQuer mostrar mais alguns termos?'))


print('{} ==> '.format(termo + tot), end= '')


