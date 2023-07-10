tupla = (int(input('Digite um numero: ')),
         int(input('Digite um numero: ')),
         int(input('Digite um numero: ')),
         int(input('Digite um numero: ')))
print(tupla)
print(tupla.count(9))
print(tupla.index(3))
for elemento in tupla:
    if elemento % 2 == 0:
        print(elemento,'',end='') 

