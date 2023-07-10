somatorio = 0
cont = 0
for impar in range(1,501,2):
    if impar % 3 == 0:
        cont = cont + 1
        somatorio = somatorio + impar
    print(impar)
print('A soma dos {} numeros Impares é: {}'.format(cont, somatorio))