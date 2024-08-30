"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
"""

numeros = list()
pares = list()
impares = list()

for c in range(1, 21):
    numeros.append(int(input(f'informe o {c}º numero: ')))
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(
    f'Os numero são {numeros}'
    f'\nOs pares são {pares}'
    f'\nOs impares são {impares}'
)





# NUMEROS = 20
# inteiros = []
# pares = []
# impares = []

# for i in range(NUMEROS):
#     numero = int(input("Digite um inteiro: "))
#     inteiros.append(numero)
#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)


# print("\nInteiros")
# for numero in inteiros:
#     print(f"{numero}", end=" ")

# print("\nPares")
# for numero in pares:
#     print(f"{numero}", end=" ")

# print("\nImpares")
# for numero in impares:
#     print(f"{numero}", end=" ")