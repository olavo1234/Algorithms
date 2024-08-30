"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = list()

for c in range(1, 5):
    notas.append(float(input(f'{c}º numero: ')))
media = sum(notas) / len(notas)

print(
    f'A media das notas foram {media}'
    f'\nA as natas foram {notas}'
)


