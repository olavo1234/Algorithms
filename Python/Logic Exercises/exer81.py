"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre
acidentes de trânsito.

Foram obtidos os seguintes dados:
    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito
        e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de
        2.000 veículos de passeio.
"""

cont_cidade_acidente = cod_maior = cod_menor = menor_indice = maior_indice = totveiculos = totacidente = 0
for c in range(1,6):
    cod_cidade = int(input('Código da cidade: '))
    veiculo_passeio = int(input('Número de veículos de passeio (em 1999): '))
    totveiculos += veiculo_passeio
    acidentes_vitimas = int(input('Número de acidentes de trânsito com vítimas (em 1999): '))
    if veiculo_passeio < 2000:
        totacidente += acidentes_vitimas
        cont_cidade_acidente += 1
    if c == 1:
        maior_indice = menor_indice = acidentes_vitimas
        cod_maior = cod_menor = cod_cidade
    else:
        if acidentes_vitimas > maior_indice:
            maior_indice = acidentes_vitimas
            cod_maior = cod_cidade
        if acidentes_vitimas < menor_indice:
            menor_indice = acidentes_vitimas
            cod_menor = cod_cidade
media_acidente = totacidente / cont_cidade_acidente
media_carro = totveiculos / 5
print(
    f'O maior indice é {maior_indice} na cidade do código {cod_maior}'
    f'\nO menor indice é {menor_indice} na cidade do código {cod_menor}'
    f'\nA média de veiculos das cidades é de {media_carro:.1f}'
    f'\nA media de acidentes de transito com menos de 2.000 carros é {media_acidente:.1f}'
)
