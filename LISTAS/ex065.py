valores = []
for c in range(5):
    num = int(input('Digite um valor: '))
    if c == 0:
        valores.append(num)
    elif num > valores[-1]:
        valores.append(num)
    else:
        pos = 0 # criou uma variavel para receber a posição
        while len(valores) > pos: # vai fazer a repetição enquanto a o tamamho da lista for maior que a posição
            if valores[pos] >= num: # se o numero daquela posiçã for maior que o numero
                valores.insert(pos, num) # vai inserir na posição o numero e o que for maior vai para a posição seguinte
                break
            pos = pos + 1 # a posição vai receber ela mais um
print(valores)