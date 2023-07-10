from math import radians,sin, cos, tan
angulo = float(input('Digite um angulo: '))
print('O angulo de {} graus, tem Seno de {:.2f} graus, Cosseno de {:.2f} graus e Tangente de {:.2f} graus'.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
