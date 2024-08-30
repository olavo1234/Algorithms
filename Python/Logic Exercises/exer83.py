"""
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos:
[0-25], [26-50], [51-75] e [76-100].

A entrada de dados deverá terminar quando for lido um número negativo.
"""



de_0_a_25 = de_26_a_50 = de_51_a_75 = de_76_a_100 = 0
while True:
    n = int(input("Digite um numero inteiro de 0 a 100 (ou negativo para parar: "))
    if n < 0:
        break
    elif n == 0 or n <= 25:
        de_0_a_25 += 1
    elif n <= 50:
        de_26_a_50 += 1
    elif n <= 75:
        de_51_a_75 += 1
    elif n <= 100:
        de_76_a_100 += 1
    else:
        print('Número inválido!')
print('Dos números digitados:')
print(
    f'Tem na lista {de_0_a_25} numeros de [0-25]'
    f'\nTem na lista {de_26_a_50} numeros de [26-50]'
    f'\nTem na lista {de_51_a_75} numeros de [51-75]'
    f'\nTem na lista {de_76_a_100} nuemros de [76-100]'
)
