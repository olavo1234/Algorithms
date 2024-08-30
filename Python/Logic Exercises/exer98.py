"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
multiplicação e os números.
"""

from math import prod

numeros = list()

for i in range(1, 6):
    numeros.append(int(input(f'Digite o {i}º numero ')))
print(
    f'A soma dos numeros {sum(numeros)}'
    f'\nA multiplicação dos foi {prod(numeros)}'
    f'\nOs numero foram {numeros}'
)
