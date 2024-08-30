"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares.
"""


quant_par = 0
quant_impar = 0
for c in range(1,11):
    numero = int(input(f'digite o {c}ª numero: '))
    if numero % 2 == 0:
        quant_par += 1
    else:
        quant_impar += 1
print(
    f"Tem {quant_par} numeros pares"
    f"\ne {quant_impar} numeros impares"
)







# vesão curta
"""
pares = 0
impares = 0
for _ in range(10):
    if int(input("Digite um numero: ")) % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Pares: {pares}\nÍmpares: {impares}")
"""