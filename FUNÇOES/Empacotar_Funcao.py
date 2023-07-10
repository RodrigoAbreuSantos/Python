def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')

#Programa Principal
contador(1,4,56,4)
contador(4,8,7,65)
contador(0,38,23)

def contador(*num):
    tamanho = len(num)
    print(f'Recebi {num} e seu tamanho é: {tamanho}')

#Programa Principal
contador(1,4,56,4)
contador(4,8,7,65)
contador(0,38,23)

def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] = lista[posicao] * 2
        posicao = posicao + 1

#Programa Principal
valores = []
for cont in range(5):
    a = int(input('Digite o numero: '))
    valores.append(a)
dobra(valores)
print(valores)



def soma(*valores):
    s = 0
    for numero in valores:
        s = s + numero
    print(f'A soma dos numeros: {valores} é: {s}')


#Programa Principal
soma(5,4,7,8,5)
soma(9,3,4,3)