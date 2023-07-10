from random import choice
from time import sleep
jokenpoMaquina = 'Pedra', 'Papel', 'Tesoura'
aleatorio = choice(jokenpoMaquina)
print('Programa Pedra Papel Tesoura')
jokenpo = input('Digite sua escolha: ')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if aleatorio == 'Pedra' and jokenpo == 'Papel':
    print('Você Ganhou')
elif aleatorio == 'Pedra' and jokenpo == 'Pedra':
    print('Empate')
elif aleatorio == 'Pedra' and jokenpo == 'Tesoura':
    print('Você Perdeu')
elif aleatorio == 'Papel' and jokenpo == 'Pedra':
    print('Você Perdeu')
elif aleatorio == 'Papel' and jokenpo == 'Papel':
    print('Empate')
elif aleatorio == 'Papel' and jokenpo == 'Tesoura':
    print('Você Ganhou')
elif aleatorio == 'Tesoura' and jokenpo == 'Papel':
    print('Você Perdeu')
elif aleatorio == 'Tesoura' and jokenpo == 'Pedra':
    print('Você Ganhou')
elif aleatorio == 'Tesoura' and jokenpo == 'Tesoura':
    print('Empate')
else:
    print('Apenas Papel Pedra ou Tesoura')
print('A escolha da maquina foi: {}'.format(aleatorio))