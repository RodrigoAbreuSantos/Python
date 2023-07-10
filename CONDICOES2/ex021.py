valorCasa= float(input("Digite o valor da sua Casa: "))
salarioComprador = float(input("Digite o salario do comprador: "))
qtdeAnosPgamento = int(input('Em quantos anos vai pagar: '))
mes = qtdeAnosPgamento * 12
prestacaoMensal = valorCasa/mes
exceder = salarioComprador*0.30
if prestacaoMensal > exceder:
    print('Emprestimo Negado') 
else:
    print('exceder = {:.2f} prestação = {:.2f}'.format(exceder, prestacaoMensal))
    # 500.000.00
    # Salario = 10000
    # 10 anos = 120 meses
    # Prestcação = 4166,66
    # exceder = 3000