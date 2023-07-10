from time import sleep
print('Contagem Regressiva.....')
for c in range(10,-1,-1):
    sleep(1)
    print('{}'.format(c))
sleep(1)
print('BOOM')