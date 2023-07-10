num = int(input('Digite um numero inteiro qualquer: '))
print('Escolha de opções: 1 = Binario. 2 = octal. 3 = Hexadecimal')
opcao = int(input("Digite a opção de conversão: "))

if opcao == 1:
    conversao = bin(num) [ 2 :]
    print(conversao)
elif opcao == 2:
    conversao = oct(num) [ 2 :]
    print(conversao)
elif opcao == 3:
    conversao = hex(num) [ 2 :]
    print(conversao)
else:
    print('Tente Novamente')
