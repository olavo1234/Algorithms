"""
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de
alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""

tot_turma = 0
tot_aluno = 0
tot_turma = int(input('Informe o numero de turmas: '))
cont = 0
while True:
    cont += 1
    aluno = int(input(f'Informe o numero total de aluno da turma {cont}: '))
    if aluno > 40:
        print('Invalido!\nAs turmas não podem ter mais de 40 alunos')
        break
    tot_aluno += aluno
    media = tot_aluno / tot_turma
    if cont == tot_turma:
        print(f'A média de alunos por tuma é de {media:.1f}')
        break
