somatorio = 0
cont = 0
for c in range(6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        cont = cont + 1
        somatorio = somatorio + num
print('Voce informou {} numero Par. A soma dos Pares é: {}'.format(cont, somatorio))
