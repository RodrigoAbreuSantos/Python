palavra = ('Aprender', 'Futuro', 'Viagem', 'Trabalho', 'Programador')
for p in palavra:
    print(f'\n Na palavra {p} temos: ', end='')
    for letra in p:
        if letra in 'AaEeIiOoUu':
            print(f'{letra}', end='')