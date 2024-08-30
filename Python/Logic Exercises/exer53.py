"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

total = 0
for i in range(1,6):
    total += float(input(f"Digite o {i}ª numero: "))
    media = total / 5
print(
    f"A soma dos mumeros é {total:,.0f}"
    f"\nA media dos numeros é {media:.1f}"
)
