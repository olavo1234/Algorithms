"""
Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.
"""

# jeito mais curto e organizado
lista = []
numero = int(input('Digite um numero: '))
escolha = str(input('precione c-continuar ou p-parar : ')).upper()
lista.append(numero)
while escolha == 'C':
    numero = int(input('Digite um numero: '))
    escolha = str(input('precione c-continuar ou p-parar : ')).upper()
    lista.append(numero)
maior = max(lista)
menor = min(lista)
soma = sum(lista)
print(
    f'O valor maximo é {maior}'
    f'\nO valor minimo é {menor}'
    f'\nA soma de tudo é {soma}'
)



# jeito mais complexo e longo
# from math import inf  # Constante 'infinito'

# # Para resolver com um laço é necessário utilizar uma lista
# numeros = []

# while True:
#     valor = input(
#         "Digite um número ou 'p' para parar e exibir os resultados: "
#     )
#     if valor.upper() == "P":
#         break
#     numeros.append(float(valor))

# menor_numero = inf
# for numero in numeros:
#     if numero < menor_numero:
#         menor_numero = numero
# print(f"O menor número é {menor_numero}")

# maior_numero = -inf
# for numero in numeros:
#     if numero > maior_numero:
#         maior_numero = numero
# print(f"O maior número é {maior_numero}")

# soma = 0
# for numero in numeros:
#     soma += numero
# print(f"A soma dos números é {soma}")
