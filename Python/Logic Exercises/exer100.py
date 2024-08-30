"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre
a soma dos quadrados dos elementos do vetor.
"""


tot = 0
a = list()

for c in range(1, 11):
    a.append(int(input(f'{c}º numero: ')))
for n in a:
    tot += (n**2)
print(f'A soma dos quadrados dos elementos do vetor é {tot}')
