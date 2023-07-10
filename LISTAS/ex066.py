valores = []
while True:
    num = int(input('Digite um numero: '))
    valores.append(num)
    resp = input('Deseja Continuar? S/N ').upper()[0]
    if resp == 'N':
        break
if 5 in valores:
    a = 'O 5 está na lista'
else:
    a = 'O 5 não está na lista'
print(f'O total de numeros digitados foram: {len(valores)}')
valores.sort(reverse=True)
print(valores)
print(a)