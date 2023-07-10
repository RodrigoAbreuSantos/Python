nome = input('Digite o nome: ').title().strip()
parte = nome.split()
print('O primeiro nome é: {} e o ultimo nome é: {}'.format(parte[0], parte[-1]))
#print('O primeiro nome é: {} e o ultimo nome é: {}'.format(parte[0], nome[len(nome)-1]))
