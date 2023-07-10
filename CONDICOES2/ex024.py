from datetime import date
tempo = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
faltante = tempo - nasc

if faltante < 18:
    a = 18- faltante
    print('Ainda vai se alistar e o tempo faltante é de: {} ano'.format(a))
elif tempo == 18:
    print('Ta na hora de se alistar')
else:
    print('Ja passou o tempo de alistamento')
