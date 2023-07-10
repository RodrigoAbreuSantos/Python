nota = float(input('Digite uma nota: '))
nota2 = float(input('Digite uma nota: '))

media = (nota + nota2)/2

if media < 5:
    print('Media = {}. Reprovado'.format(media))
elif media >= 5 and media < 7:
    print('Media = {}. Recuperação'.format(media))
else:
    print('Media = {}. Aprovado'.format(media))