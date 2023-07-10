import datetime
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = datetime.date.today().year
tempo = ano_atual - ano_nasc

if tempo <= 9:
    print('Mirim')
elif tempo > 9 and tempo <= 14:
    print('Infantil')
elif tempo > 14 and tempo <= 19:
    print('Junior')
elif tempo > 19 and tempo <= 20:
    print('Senior')
else:
    print('Master')