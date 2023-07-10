''' 
Interactive Help ==> help(print). O help ele é meio que um manual de ajuda 
que mostra como serve determinada coisa em python. 
print(input.__doc__) ==> tipo um help só que de outra maneira
DocStrings ==> 

def contador(i, f, p):
    ''''''
    ==> Faz uma contagem e mostra na tela
    parametro i ==> inicio da contagem 
    parametro f ==> fim da contagem 
    parametro p ==> passo da contagem 
    ''''''
    c = i
    while c <= f:
        print(f'{c}',end=' ')
        c += p

help(contador)

Argumentos Opcionais ==>

def somar(a=0, b=0, c=0):
    ''''''
    Soma de 3 valores
    parametro a: 1 valor
    parametro b; 2 valor
    parametro c: 3 valor
    ''''''
    s = a+b+c
    print(f'A soma vale {s}')
somar()
somar(3,3)

Escopo de Variaveis ==>

def teste():
    x = 8 VARIAVEL LOCAL, POIS VAI FUNCIONAR APENAS DENTRO DA FUNÇÃO
    print(f'Na função teste, n vale{n}')
    print(f'Na função teste, x vale{x}')

n = 2 VARIAVEL GOLOBAL, POIS VAI FUNCIONAR DENTRO E FORA DA FUNÇÃO
print(f'Na função teste, n vale{n}')
teste()
print(f'Na função teste, x vale{x}') Esse vai dar erro, pois x é uma variavel local


Retorno de Resultados ==> Serve para mandar o resultado, não para escrever da maneira que vc quiser

def somar(a=0, b=0, c=0):
    s = a+b+c
    return s

r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)
print(f'Meus calculos foram {r1},{r2} e {r3}')
'''


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    return f

num = int(input('Digite um numero: '))
print(f'Os resultados de {num} é {fatorial(num)}')


def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
if par(num):
    print('É par')
else:
    print('É impar')
