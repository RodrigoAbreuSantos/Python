print("\033[0;32m Ola Mundo \033[m") # o comando para cor é \033[style; text; back m \033[m
a = 3
b = 5
print("Os valores são \033[0;33m{}\033[m e \033[0;31m{}\033[m". format(a,b))
print("Os valores são: {}{} e {}{}".format('\033[33m', a,b, '\033[m'))
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;30m'
}
print('Os valores são: {}{} e {}{}'.format(cores['amarelo'], a, b, cores['limpa']))