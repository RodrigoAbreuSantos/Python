num = 0
somatorio = 0
cont = 0
while num != 999:
    num = int(input('Digite um numero: '))
    if num != 999:
        cont = cont + 1
        somatorio = somatorio + num
print('Foram digitados {} numeros e a soma deles é: {}'.format(cont, somatorio))