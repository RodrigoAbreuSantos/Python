while True:
    num = int(input('Digite um numero: '))
    if num > 0:
        for c in range(1,11):
            print(f'{num} x {c} = {num*c}')
    if num < 0:
        break