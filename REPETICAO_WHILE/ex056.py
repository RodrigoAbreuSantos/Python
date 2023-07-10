valor = int(input('Qual o valor a ser sacado? '))
tot = valor
cred = 50
totCred = 0
while True:
    if tot >= cred:
        tot = tot - cred
        totCred = totCred + 1
    else:
        if totCred > 0:
            print(f'Total de {totCred} cedulas de {cred}R$')
        if cred == 50:
            cred = 20
        elif cred == 20:
            cred = 10
        elif cred == 10:
            cred = 1
        totCred = 0
        if tot == 0:
            break
