cidade = input('Digite o nome de uma cidade: ').strip().capitalize()
parte = cidade.split()
if parte[0] == 'Santo':
    print('Esta cidade começa com a palavra Santo')
else:
    print('Esta cidade não começa com a palavra Santo')