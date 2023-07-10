valor = float(input('Digite o valor a ser pago: '))
print('1 - Dinheiro/Cheque. 2- A Vista no Cartão. 3 - 2x no Cartão. 4- 3x ou mais no Cartão')
condicao = int(input('Forma de Pagamento: '))

if condicao == 1:
    desc = (valor*0.10)
    valor2 = valor - desc
    print('O valor a ser pago sera: {:.2f}'.format(valor2))
elif condicao == 2:
    desc = (valor*0.05)
    valor2 = valor - desc
    print('O valor a ser pago sera: {:.2f}'.format(valor2))
elif condicao == 3:
    valor2 = valor
    print('O valor a ser pago sera: {:.2f}'.format(valor2))
elif condicao == 4:
    juros = (valor*0.20)
    valor2 = valor + juros
    print('O valor a ser pago sera: {:.2f}'.format(valor2))
else:
    print('Opção Invalida')
