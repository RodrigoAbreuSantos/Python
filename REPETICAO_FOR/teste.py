cont = 0
for c in range(0,4):
    cont = cont +1
    print('Oi = {}'.format(cont))
print('Total de Oi = {}'.format(cont))

# coloquei de 0 ate 4, porque seu colocasse de 1 ate 4 ele iria fazer de 1 ate 3 e no 4 ele para
# ele não considera o ultimo numero

# OBS: for c in range(0,4)
# vai procurar o c dentro do intervalo. Ou seja se eu desse um print(c) dentro do o resultado seria:
# 0 
# 1
# 2
# 3

for c in range(4,0,-1):
    print('{} = Oi'.format(c))

# range(onde começa, onde termina, e iteração)
# iteração ==> padrão que seguira se vai de 1 em 1, 2 em 2, de -1 em -1 etc

n = int(input('Digite um Numero: '))
for c in range(0,n+1):
    print(c)
print('Fim')

i = int(input('Digite o Inicio: '))
p = int(input('Digite o Passo: '))
f = int(input('Digite o Fim: '))

for c in range(i,f+1,p):
    print(c)
print('FIM')

somatorio = 0
for c in range(0,4):
    n = int(input('Digite um Numero: '))
    somatorio = somatorio + n
print('O somatorio é de: {}'.format(somatorio))