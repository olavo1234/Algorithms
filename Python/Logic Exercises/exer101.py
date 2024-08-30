"""
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos
pelos elementos intercalados dos dois outros vetores.
"""


vetor1 = list()
vetor2 = list()
conjunto = list()

for i in range(1,11):
    vetor1.append(int(input(f'Informe o {i}º valor do 1º vetor: ')))
for i in range(1,11):
    vetor2.append(int(input(f'Informe o {i}º valor do 2º vetor: ')))
for i in range(0,10):
    conjunto.append(vetor1[i])
    conjunto.append(vetor2[i])
print('CONJUNTO INTERCALADO')
for c in conjunto:
    print(c,end=' ')
