valores = []
valores2 = []
valores3 = []
while True:
    num = int(input('Digite um numero: '))
    valores.append(num)
    resp = input('Deseja Continuar? S/N ').upper()[0]
    if resp == 'N':
        break
for pos, valor in enumerate(valores):
    if valor % 2 == 0:
        valores2.append(valor)
    else:
        valores3.append(valor)

print(valores)
print(valores2)
print(valores3)