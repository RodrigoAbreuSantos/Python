def area(largura, comprimento):
    areaTerreno = largura*comprimento
    print(f'A area do terreno de largura {largura} e comprimento {comprimento} é: {areaTerreno}')

#Programa Principal
num1 = float(input('Digite a Largura: '))
num2 = float(input('Digite o Comprimento: '))
area(num1, num2)