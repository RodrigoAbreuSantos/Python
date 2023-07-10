from datetime import date
cadastro = {}
for cont in range(1):
    cadastro['Nome'] = input('Digite seu Nome: ') 
    cadastro['Idade'] = int(input('Digite o Ano de Nascimento: '))
    cadastro['CTPS'] = int(input('Digite sua Carteira (0 não tem): '))
cadastro['Idade'] = date.today().year - cadastro['Idade']
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = input('Digite o Ano de Contratação: ')
    cadastro['Salario'] = float(input('Digite seu salario: R$'))
    cadastro['Aposentadoria'] = 75 - cadastro['Idade']
    print('-=-'*30)
    for chave, valor in cadastro.items():
        print(f'{chave} ==> {valor}')
else:
    print('-=-'*30)
    for chave, valor in cadastro.items():
        print(f'{chave} ==> {valor}')