def voto(ano_nascimento):
    from datetime import date
    tempo = date.today().year
    votacao = tempo - ano_nascimento
    if votacao < 16:
        return f'Com {votacao} anos. Voto Negado'
    elif votacao >= 16 and votacao < 18:
        return f'Com {votacao} anos. Voto Opcional'
    else:
         return f'Com {votacao} anos. Voto Obrigatorio'

#Programa Principal
anoNascimento = int(input('Digite o ano de nascimento: '))
print(voto(anoNascimento))
