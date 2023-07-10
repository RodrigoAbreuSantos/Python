expressao = input('Digite uma expressão: ')
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append(expressao)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Correto')
else:
    print('Incorreto')
