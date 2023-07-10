somatorio = cont = 0
lista = []
while True:
    num = int(input('Digite um numero: '))
    cont = cont + 1
    somatorio = somatorio + num
    lista.append(num)
    resp = input('Deseja continuar? ').upper()[0]
    if resp not in 'SN':
        print('Tente novamente')
    if resp == 'N':
        break
menor = min(lista)
maior = max(lista)
media = somatorio/cont
print('A media é: {} e o maior valor digitado foi: {} e o menor foi: {}'.format(media, maior, menor))