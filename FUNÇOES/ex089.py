def notas(*n):
    dicio = dict()
    dicio['qtde'] = len(n)
    dicio['Maior'] = max(n)
    dicio['Menor'] = min(n)
    dicio['Media'] = sum(n)/len(n)
    if dicio['Media']>= 7:
        dicio['Situaçao'] = 'BOM'
    elif dicio['Media']>= 5 and dicio['Media']< 7:
      dicio['Situaçao'] = 'RAZOAVEL'
    else:
       dicio['Situaçao'] = 'RUIM'

    return dicio


#Programa Principal
resp = notas(5.5, 6.5, 4)
print(resp)