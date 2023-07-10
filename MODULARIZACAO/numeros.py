#import uteis ==> está importando o modulo uteis
#from uteis import fatorial,dobro,triplo ==> dentro do modulo uteis está importando as funções fatoriais, dobro e triplo
import uteis

num = int(input('Digite o numero: '))
fat = uteis.fatorial(num)
dobro = uteis.dobro(num)
triplo = uteis.triplo(num)
print(f'O fatorial de {num} é: {fat}, o dobro é: {dobro} e o triplo é: {triplo}')