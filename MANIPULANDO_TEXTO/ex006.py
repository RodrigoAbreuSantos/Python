frase = input('Digite uma frase: ')
if len(frase) > 20: #len vai pegar o comprimento da string, faz parte da Analise
    #Fatiamento
    print(frase[::3])#vai do começo até o fim pulando de 3 em 3, então se digitar Rodrigo ele print o R e pula 3 e print o r e assim vai indo
    print(frase[2:8])# iria do espaço 2 até o espaço 7, pois desconsidera o ultimo
    print(frase[:8])#iria do começo até o espaço 7, pois desconsidera o ultimo
    print(frase[2:8:2])#iria do espaço 2 até o espaço 7, pois desconsidera o ultimo. Pulando de 2 em 2
    print(frase[2::2])#iria do espaço 2 até o fim, pulando de 2 em 2
    #Analise
    print('Analise')
    print(frase.count('o'))#Ira contar quantas vezes aparece a letra o
    print(frase.count('o', 0, 13))#Ira contar quantas vezes aparece a letra o do espaço zero até o espaço 12
    print(frase.find('eu'))#ira dizer quando encontrou o conjunto de palavras digitadas, começando pela posição que iniciou. Então se inivio na posição 10 ira imprimir 10 na tela
    print(frase.find('Android'))#Se você colocar uma parte da string que não existe ira retornar -1, signifca que não foi encontrado na string
    print('Rodrigo' in frase)# se existir Rodrigo na frase ele vai retornar True, quaso não exista ira retornar False
    #Transformação
    print('Transformação')
    print(frase.replace('Santos', 'Anjos'))#ira mudar o Santos da string para Anjos
    print(frase.upper())#Ira colocar toda a string em maiusculo
    print(frase.lower())#Ira colocar toda a string em minusculo
    print(frase.capitalize())#Ira jogar toda a string para minusculo e apenas o primeiro espaço da string para maiusculo
    print(frase.title())#Toda letra depois do espaço é transformada em maiusculo, e a primeira posição tambem sera maiuscula
    print(frase.strip())#Ira remover todos os espaços inuteis no começo e no fim da string, os espaços restantes serão mantidos
    print(frase.rstrip())#ira remover somente os ultimos espaços inuteis da string
    print(frase.lstrip())#ira remover somente os espaços inuteis do começo da string
    #Divisão
    print(frase.split())#o split vai divider os elementos em uma lista, onde cada elemento vai ser separado pelo espaço. Ex: Curso em Video ==> A primiera parte da lista é curso logo em seguida em e por ultimo Video. Onde Curso tem indice 0 em indice 1 e Video indice 2
    #Junção
    print('-'.join(frase))#Se você tem alguma coisa separada em listas, como o split por exemplo. O join vai juntar tudo, gerando uma string unica. E o '-' significa que onde havia espaços tera um -. Caso você queira um espaço normal é so colocar ''
    

else:
    print('Frase curta')