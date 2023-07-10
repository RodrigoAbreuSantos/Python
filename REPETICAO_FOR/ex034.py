tabuada = int(input('A tabuada vai até que numero? '))
num = int(input('Qual o numero para a Tabuada? '))
for numTab in range(1,tabuada+1):
    mult = numTab * num
    print('{} x {} = {}'.format(num,numTab,mult))