time = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avai', 'Ponte-Preta', 'Atlético-GO')

# A) 5 - Primeiros Colocados
print(time[:5])

# B) 4 - Ultimos Colocados
print(time[-4:])

# C) Ordem Crescente
print(sorted(time))

# D) Em que posição esta a Chapecoense
print(time.index('Chapecoense')+1)