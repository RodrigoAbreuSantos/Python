somatorio = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    somatorio = somatorio + num
print(f'A soma é: {somatorio}')