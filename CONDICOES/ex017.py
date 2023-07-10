distancia = float(input('Digite a distancia da viagem em KM: '))
preco = 0.50*distancia if distancia <= 200 else 0.45*distancia
print('O preço da passagem foi de: {:.2f}'.format(preco))
