"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus
telespectadores para saber qual o melhor jogador após cada jogo.
Para isto, faz-se necessário o desenvolvimento de um programa, que será
utilizado pelas telefonistas, para a computação dos votos.
Sua equipe foi contratada para desenvolver este programa.
Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
correspondente ao número da camisa do jogador.
Um número de jogador igual zero, indica que a votação foi encerrada.
Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma
breve mensagem de aviso, e voltando a pedir outro número.
Após o final da votação, o programa deverá exibir:

    O total de votos computados;

    Os números e respectivos votos de todos os jogadores que receberam votos;

    O percentual de votos de cada um destes jogadores;

    O número do jogador escolhido como o melhor jogador da partida,
        juntamente com o número de votos e o percentual de votos dados a ele.

    Observe que os votos inválidos e o zero final não devem ser computados
        como votos.

    O resultado aparece ordenado pelo número do jogador.

    O programa deve fazer uso de arrays.

    O programa deverá executar o cálculo do percentual de cada jogador
        através de uma função. Esta função receberá dois parâmetros:
            o número de votos de um e o total de votos.

    A função calculará o percentual e retornará o valor calculado.

Exemplo:
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9       4               50,0% é uma lista dentro de uma lista
10      3               37,5% é outra lista dentro de outra lista
11      1               12,5%
O melhor jogador foi o número 9, com 4 votos,
correspondendo a 50% do total de votos.
"""


jogadores_total = list()
# \\
# listas para exibir
dados_jogador = list()
dados_votos = list()
dados_porcentagem = list()

print('Enquete: quem foi o melhor jogador?')
print()
while True:
    numero_camisa = int(input('Numero do jogador (0 = FIM): '))
    if numero_camisa == 0:
        break    
    elif numero_camisa < 1 or numero_camisa > 23:
        print('Inválido, somente numero de 1 a 23,',end=' ')
        continue
    jogadores_total.append(numero_camisa)
    #\\
    # if para não repetir numeros
    if numero_camisa not in dados_jogador:
        dados_jogador.append(numero_camisa)
#\\
# vai contar o numero de votos dos jogadores
for c in dados_jogador:
        dados_votos.append(jogadores_total.count(c))
tot_votos = sum(dados_votos)
#\\


def calcular_porcent(n_votos, total):
    return ((n_votos / total) * 100)


for v in dados_votos:
    resultado = calcular_porcent(v, tot_votos)
    dados_porcentagem.append(resultado)

# \\

# demonstração de resultados:
print()
print('Resultado da votação:')
print()
print(f'Foram computados {tot_votos} votos.')
print()
print('Jogador\t\tVotos\t%')
for c in range(0, len(dados_jogador)): 
    print(f'{dados_jogador[c]}\t\t{dados_votos[c]}\t{dados_porcentagem[c]:.2f}')
print()

melhor_resul = dados_votos.index(max(dados_votos))
print(
    f'O melhor jogador foi o número {dados_jogador[melhor_resul]}, com {dados_votos[melhor_resul]} votos,'
    f'\ncorrespondendo a {dados_porcentagem[melhor_resul]:.2f}% do total de votos.'
)
