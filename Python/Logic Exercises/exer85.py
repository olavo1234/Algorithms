"""
Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código.
Os códigos utilizados são:
    1, 2, 3, 4  - Votos para os respectivos candidatos
    (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco

Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos.

Para finalizar o conjunto de votos tem-se o valor zero.
"""

tot_voto = tot_nulo = tot_branco = 0
cand_1 = cand_2 = cand_3 = cand_4 = 0
print("ELEIÇÃO PRESIDENCIAL - VOTAÇÃO")
print("""
1 - José
2 - João
3 - Maria
4 - Joaquim
5 - Voto Nulo
6 - Voto em Branco
""")
print("-"*30)
while True:
    voto = int(input('Informe o seu voto: (0 para finalizar) '))
    if voto == 0:
        break
    else:
        if voto <= 4:
            tot_voto += 1
    if voto == 1:
        cand_1 += 1
    elif voto == 2:
        cand_2 += 1
    elif voto == 3:
        cand_3 += 1
    elif voto == 4:
        cand_4 += 1
    elif voto == 5:
        tot_nulo += 1 
    elif voto == 6:
        tot_branco += 1
    else:
        print('Voto invalido!')
        tot_voto -= 1
porcentagem_nulo = (tot_nulo * tot_voto) / 100
porcentagem_branco = (tot_branco * tot_voto) / 100
print("-"*30)
print(
    f'total de votos para jose {cand_1}'
    f'\ntotal de votos para joão {cand_2}'
    f'\ntotal de votos para maria {cand_3}'
    f'\ntotal de votos para joaquim {cand_4}'
    f'\ntotal de votos nulos {tot_nulo}'
    f'\ntotal de votos em branco {tot_branco}'
    f'\n{tot_nulo} votos anulados com um total de {porcentagem_nulo:.2f}%'
    f'\n{tot_branco} votos em branco com um total de {porcentagem_branco:.2f}%'
)
print("-"*30)
