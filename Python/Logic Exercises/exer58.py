"""
Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

base = float(input("digite o valor da base: "))
expoente = int(input("digite o valor do expoente: "))
total = 1
for c in range(expoente):
    total *= base 
print(f"A base {base:,.2f} com o expoente {expoente} resultado é {total:,.2f}")
