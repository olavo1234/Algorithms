"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem
inversa a ordem lida.
"""

# ESSA TEM 2 FORMAS DE RESOLVER PORQUE É MAL EXPLICADO


idades = list()
alturas = list()

for i in range(1, 6):
    idades.append(int(input(f'Informe a idade da {i}ª pessoa: ')))
    alturas.append(float(input(f'Informe a altura da {i}ª pessoa: ')))
idades.reverse()
alturas.reverse()
print(
    f'A idade na ordem inversa lida é {idades}'
    f'\nA altura na ordem inversa lida é {alturas}'
)


PESSOAS = 5
idades = []
alturas = []
for i in range(PESSOAS):
    idades.append(int(input(f"Digite a idade da pessoa {i+1}: ")))
    alturas.append(float(input(f"Digite a altura da pessoa {i+1} em cm: ")))

# ? i começa em 4 e vai até 0 de forma decrescende
for i in range(PESSOAS - 1, -1, -1):
    print(f"A pessoa {i+1} mede {alturas[i]:.2f}cm e tem {idades[i]} ano(s)")
