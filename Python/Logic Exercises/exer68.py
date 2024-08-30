"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""

total = 0
cont = 0
while True:
    n = float(input('Digite o valor da nota: '))
    cont += 1
    total += n
    media = total / cont
    resp = str(input('Diigte [S/N] para continuar: '))
    if resp in 'Nn':
        break
print(f'A média é de {media:.2f}')

