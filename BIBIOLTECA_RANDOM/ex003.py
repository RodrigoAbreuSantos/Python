from random import choice

lista = [] #criar uma lista que contera uma variavel
for x in range(0,5,1): #repetir 5 vezes o que tiver dentro do for
    nome = input('Digite seu nome: ').upper()
    lista.append(nome) #criar o append para conter uma variavel dentro da lista 
print(choice(lista)) # usando o import eu selecio um nome aleatorio dentro da lista