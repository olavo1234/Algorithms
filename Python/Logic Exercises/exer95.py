"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes
foram lidas. Imprima as consoantes.
"""
cont = 0
caracter = list()

for c in range(1,11):
    caracter.append(str(input('Digite os caracteres: ')).upper())
if 'A' in caracter:
    cont += 1
    caracter.remove('A')
if 'E' in caracter:
    cont += 1
    caracter.remove('E')
if 'I' in caracter:
    cont += 1
    caracter.remove('I')
if 'O' in caracter:
    cont += 1
    caracter.remove('O')
if 'U' in caracter:
    cont += 1
    caracter.remove('U')

print('\nAs cosoantes são:')
for car in caracter:
    print(car,end=' ')
print(f'Foram lidas {cont} consantes')
