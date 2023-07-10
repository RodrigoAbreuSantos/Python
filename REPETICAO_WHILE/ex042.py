sexo = input('Digite seu sexo: ').upper()[0]
while sexo not in 'MF':
    sexo = input('Tente Novamente. Digite seu sexo: ').upper()[0]
print('Informações Corretas')