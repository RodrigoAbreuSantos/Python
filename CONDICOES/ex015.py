velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    sub = velocidade - 80
    multa = 7*sub
    print('Você foi Multado e sua multa foi de R${:.2f} reais'.format(multa))
