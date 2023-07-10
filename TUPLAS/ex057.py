tupla = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
tupla2 = ('Zero', ' Um', 'Dois', 'Tres', 'Quatro', 'CInco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um numero entre 0 e 20: '))
cont = 0
for numero in tupla:
    cont = cont + 1
    if num == numero:
        print(f'Você digitou o numero: {tupla2[cont-1]}')

print({tupla2[num]})