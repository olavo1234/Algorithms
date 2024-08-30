"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem
inversa.
"""


numeros = list()

for i in range(1, 6):
    numeros.append(int(input(F'{i}º numero: ')))
numeros.sort(reverse=True)

print(
    f'Os numeros na ordem reversa são: {numeros}'
)


# numeros = []
# for i in range(10):
#     numeros.append(float(input(f"Digite o {i+1}º numero real: ")))
# print("Os numeros inversos são: ", end="")
# for numero in numeros[::-1]:
#     print(f" {numero}", end="")
