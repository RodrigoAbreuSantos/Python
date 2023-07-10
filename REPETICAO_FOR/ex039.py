from datetime import date
cont = 0
cont2 = 0
for ano in range(7):
    ano_nasc = int(input('Em que ano a {} Pessoa Nasceu: '.format(ano+1)))
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    if idade < 18:
        cont = cont + 1
    else: 
        cont2 = cont2 + 1
print('O total Pessoa que são maiores de Idade são: {} e o total de menores são: {}'.format(cont2, cont))