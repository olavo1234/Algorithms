"""
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato.
"""



candidato1 = 0
candidato2 = 0
candidato3 = 0
quant = int(input('Informe a quantidade de eleitores: '))
print("""qual candidato que votar ?
Candidato 1 
Candidato 2 
Candidato 3
""")
for c in range(1,quant+1):
    voto = int(input(f'Eleitor nº {c} informe o numero do candidato: '))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
print(
    '\nVotação ENCERRADA!'
    f'\nCANDIDATO 1 votos: {candidato1}'
    f'\nCANDIDATO 2 votos: {candidato2}'
    F'\nCANDIDATO 3 votos: {candidato3}'
)
