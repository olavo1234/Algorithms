"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são
eliminados.

O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe a média dos saltos conforme a
descrição acima informada (retirar o melhor e o pior salto e depois
calcular a média).

Faça uso de uma lista para armazenar os saltos.
Os saltos são informados na ordem da execução, portanto não são ordenados.
O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:
    Atleta: Rodrigo Curvêllo

    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m

    Melhor salto:  6.5 m
    Pior salto: 5.3 m
    Média dos demais saltos: 5.9 m

    Resultado final:
    Rodrigo Curvêllo: 5.9 m
"""

# solução com listas compostas

# bibliotacas
# from os import system
# from sys import platform
# if platform == 'win32':
#     limpar = 'cls'
# else:
#     limpar = 'clear'

# # listas
# dado = list()
# atletas = list()
# contagem = ['Primeiro','Segundo','Terceiro','Quarto','Quinto']
# saltos = list()

# while True:
#     print('')
#     nome_atleta = str(input('Nome do atleta ou (Enter para parar): ')).strip()
#     if nome_atleta == '':
#         break
#     for c in contagem:
#         saltos.append(float(input(f'{c} Salto: ')))
#     maior = max(saltos)
#     menor = min(saltos)
#     saltos.remove(maior)
#     saltos.remove(menor)
#     media = sum(saltos) / 3
#     system(limpar)
#     print(
#         f'Atleta: {nome_atleta}'
#         f'\nO melhor salto foi de {maior}'
#         f'\nO pior salto foi de {menor}'
#     )
#     print(f'Média dos demais saltos {media:.2f} m')
#     dado.append(nome_atleta)
#     dado.append(media)
#     atletas.append(dado[:])
#     dado.clear()
#     saltos.clear()
#     continue
# print('\n\tRESULTADO FINAL')
# print('')
# for atleta in atletas:
#     print(f'{atleta[0]}: {atleta[1]}')




# solução com dicionários

atletas = []

while True:
    nome = input(
        "Digite o nome do atleta ou enter para continuar: "
    )
    if nome == '':
        break
    atleta = {
        "nome": nome,
        "saltos": [],
        "media": 0,
        "melhor_salto": 0,
        "pior_salto": 0
    }
    for i in range(5):
        atleta.get("saltos").append(
            float(input(f'Distancio do {i+1}ª salto: '))
        )
    atleta.get("saltos").sort() # ordernar a lista
    atleta["pior_salto"] = atleta.get("saltos").pop(0)
    # essa chave pegará o primeiro valor da lista e irá removela da lista
    atleta["melhor_salto"] = atleta.get("saltos").pop(0)
    # mesma coisa aqui so que pegando/removendo o ultimo
    atleta["media"] = sum(atleta.get("saltos")) / 3
    # media irá eceber a soma da lista e a divisão pelo restante
    print(
        f'\nMelhor salto: {atleta.get("melhor_salto"):.1f} m'
        f'\nPior salto: {atleta.get("pior_salto"):.1f} m'
        f'\nA média dos demais saltos: {atleta.get("media"):.1f} m\n'
    )
    atletas.append(atleta)

print("\n\nResultado final")
for atleta in atletas:
    print(f'{atleta.get("nome")}: {atleta.get("media"):.1f} m')
