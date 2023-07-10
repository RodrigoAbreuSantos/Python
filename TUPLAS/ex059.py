from random import randint
tupla = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
cont = 0
for elemento in tupla:
    cont = cont + 1
    if cont == 1:
        maior = elemento
    if elemento > maior:
        maior = elemento
print(tupla)
print(f'O maior valor é {maior} ou {max(tupla)}')
print(f'O menor valor é {min(tupla)}')
