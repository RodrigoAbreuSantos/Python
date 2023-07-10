tupla = ('Arroz' , 20,
        'Feijão', 25, 
        'Macarrão', 15, 
        'Azeite', 8, 
        'Maçã', 5,
        'Pera', 4
        )

for posProd in range(0,len(tupla)):
    if posProd % 2 == 0:
        print(f'{tupla[posProd]}.......', end='')
    else:
        print(f'{tupla[posProd]}')