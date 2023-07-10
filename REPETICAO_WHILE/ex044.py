print('Menu de Escolhas ==>\n [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos Numeros\n [5] Sair do Programa')
valor1 = float(input('Digite o valor 1: '))
valor2 = float(input('Digite o valor 2: '))
while True: 
        escolha = int(input('Digite sua escolha: '))
        if escolha == 1:
            soma = valor1 + valor2
            print('A soma é: {}'.format(soma))
        elif escolha == 2:
            mult = valor1 * valor2
            print('A mult é: {}'.format(mult))
        elif escolha == 3:
            if valor1 > valor2:
                maior = valor1
            else: 
                maior = valor2
            print('O maior valor é: {}'.format(maior))
        elif escolha == 4:
            valor1 = float(input('Digite o valor 1: '))
            valor2 = float(input('Digite o valor 2: '))
        else:
            print('FIM')
            break
