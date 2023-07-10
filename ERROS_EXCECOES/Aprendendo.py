'''
try:
    OPERAÇÃO
except:
    FALHA
else:
    DEU CERTO
finally:
    DEU CERTO OU FALHA. Acontece independente do resultado
'''

try:
    a = float(input('Numero: '))
    b = float(input('Numero: '))
    r = a/b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados digitados')
except ZeroDivisionError:
    print('Não é possivel divisão por zero')
except KeyboardInterrupt:
    print('O usuario preferiu não digitar os dados')
except Exception as erro:
    print(f'Problema encontrado foi: {erro.__class__}')
else:
    print(f'O resultado foi: {r:.1f}')
finally:
    print('Obrigado. Volte Sempre')