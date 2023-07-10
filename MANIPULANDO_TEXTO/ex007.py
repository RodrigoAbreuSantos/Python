nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
primeiroNome = nome.split()#O total da primeira parte da string
espaco = len(nome) - nome.count(' ')#O tota da string sem os espaços
print(espaco)
print(len(primeiroNome[0]))

