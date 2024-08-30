"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

# jeito mais organizado
lista = []
numero = int(input('Digite um numero: '))
while numero < 0 or numero > 1000:
    print('invalido, tente novamente!')
    numero = int(input('Digite um numero: '))
else:
    lista.append(numero)
escolha = str(input('precione c-continuar ou p-parar : ')).upper()

while escolha == 'C':
    numero = int(input('Digite um numero: '))
    while numero < 0 or numero > 1000:
        print('invalido, tente novamente!')
        numero = int(input('Digite um numero: '))
    else:
        lista.append(numero)
    escolha = str(input('precione c-continuar ou p-parar : ')).upper()
maior = max(lista)
menor = min(lista)
soma = sum(lista)
print(
    f'O valor maximo é {maior}'
    f'\nO valor minimo é {menor}'
    f'\nA soma de tudo é {soma}'
)




# jeito mais longo
# from math import inf  # Constante 'infinito'

# # Para resolver com um laço é necessário utilizar uma lista
# numeros = []

# while True:
#     valor = input(
#         "Digite um número entre 0 e 1000 "
#         "ou 'p' para parar e exibir os resultados: "
#     )
#     if valor.upper() == "P":
#         break
#     valor = float(valor)
#     if 0 <= valor <= 1000:
#         numeros.append(valor)

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