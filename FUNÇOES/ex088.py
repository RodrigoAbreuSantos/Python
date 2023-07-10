def leiaInteiro(msg):
    valor = 0
    while True:
        numero = input(msg)
        if numero.isnumeric():
            valor = int(numero)
            break
        else:
            print('Erro! Digite um numero valido')

    return valor

#Programa Principal
numero = leiaInteiro('Digite um numero: ')
print(f'Voce acabou de digitar o numero: {numero}')


'''Explicação Exercicio ==> Primeiramente criou uma função que como parametro tinha uma mensagem
e a variavel global numero recebia a função e transformava o parametro como texto e depois transforma
em um numero inteiro criando uma outra varivel chamada valor. depois retornava o valor e mostrava o valor
'''