"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

numeros = list()
for i in range(1,6):
    numeros.append(int(input(f'{i}º Numero: ')))

print('Resultado:', end=' ')
for numero in numeros:
    print(numero, end=' ')
