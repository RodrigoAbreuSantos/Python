primeiroTermo = int(input('Digite o Primeiro Termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
decimoTermo = primeiroTermo + (10-1) * razao
for elemento in range(primeiroTermo, decimoTermo + razao, razao):
    print('{}'.format(elemento), end =' ==> ')
print('Acabou', end=' ')