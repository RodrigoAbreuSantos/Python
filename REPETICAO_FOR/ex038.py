for f in range(5):
    frase = input('Digite uma Frase: ').strip().upper()
    separarFraseLista = frase.split()
    juntar = ''.join(separarFraseLista)
    frase_invertida = frase[::-1].upper()
    separarFraseInvertidaLista = frase_invertida.split()
    juntar2 = ''.join(separarFraseInvertidaLista)
    print(frase_invertida)
    if juntar == juntar2:
        print('É um palindromo. {} = {}'.format(juntar, juntar2))
    else:
        print('Não é um palindromo. {} != {}'.format(juntar, juntar2))