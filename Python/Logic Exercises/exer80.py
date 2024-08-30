"""
Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando
a sua altura em centímetros.

Encontre o aluno mais alto e o mais baixo.

Mostre o número do aluno mais alto e o número do aluno mais baixo,
junto com suas alturas.
"""

baixo = alto = num_baixo = num_alto = 0

for c in range(1,11):
    num_aluno = int(input('Numero do aluno: '))
    altura = float(input('Altura do aluno: '))
    if c == 1:
        baixo = alto = altura
        num_baixo = num_alto = num_aluno
    else:
        if altura > alto:
            alto = altura
            num_alto = num_aluno
        if altura < baixo:
            baixo = altura
            num_baixo = num_aluno
print(
    f'O numero do aluno {num_baixo} é o mais baixo com {baixo}'
    f'\nO numero do aluno {num_alto} é o mais alto com {alto}'
)
