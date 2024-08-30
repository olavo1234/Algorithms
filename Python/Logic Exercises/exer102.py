"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

vetor1 = list()
vetor2 = list()
vetor3 =list()
conjunto = list()

for i in range(1,11):
    vetor1.append(int(input(f'Informe o {i}º valor do 1º vetor: ')))
for i in range(1,11):
    vetor2.append(int(input(f'Informe o {i}º valor do 2º vetor: ')))
for i in range(1,11):
    vetor3.append(int(input(f'Informe o {i}º valor do 3º vetor: ')))
for i in range(0,10):
    conjunto.append(vetor1[i])
    conjunto.append(vetor2[i])
    conjunto.append(vetor3[i])
print('CONJUNTO INTERCALADO')
for c in conjunto:
    print(c,end=' ')
