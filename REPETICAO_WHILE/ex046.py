primeiroTermo = int(input('Digite o Primeiro Termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiroTermo
cont = 1
while cont <= 10:
    cont += 1
    print('{} ==> '.format(termo), end= '')
    termo = termo + razao
print('Acabou')







'''for elemento in range(primeiroTermo, decimoTermo + razao, razao):
    print('{}'.format(elemento), end =' ==> ')
print('Acabou', end=' ')'''