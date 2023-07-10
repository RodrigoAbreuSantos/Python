num = int(input('Digite um numero: '))
total = 0
for numPrimo in range(1, num + 1):
    if num % numPrimo == 0:
        total = total + 1
        print('\033[33m', end= '')
    else:
        print('\033[31m', end = '')
    print(numPrimo, end= ' ')
print('\n O {} foi divisel por {} numeros'.format(num, total))
if total == 2:
    print('Numero Primo')