def titulo(txt):
    print('-=-'*15)
    print(txt)
    print('-=-'*15)


#Programa Principal
titulo('Sistema de Alunos')
titulo('Cadastro de Funcionarios')
titulo('Erro no Sistema')

a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)
'''Ao inves de fazer isso pode usar uma função'''
def soma(a, b):
    s = a+b

#Programa Principal
soma(4,5)
soma(8,9)
soma(2,1)