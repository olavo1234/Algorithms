"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média.

A atribuição de conceitos obedece à tabela abaixo:
    Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0         A
    Entre 7.5 e 9.0          B
    Entre 6.0 e 7.5          C
    Entre 4.0 e 6.0          D
    Entre 4.0 e zero         E

O algoritmo deve mostrar na tela as notas, a média,
o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
ou “REPROVADO” se o conceito for D ou E.

passos
ler e entender o que se esta sendo pedido
pedir duas notas ao usuario de uma disciplina e calcular a media
para a atribuição de conceito abedecer a sequinte tabela:

 Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0         A
    Entre 7.5 e 9.0          B
    Entre 6.0 e 7.5          C
    Entre 4.0 e 6.0          D
    Entre 4.0 e zero         E

exibir ao usuario as sequintes informações:
as notas, a média,
o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
ou “REPROVADO” se o conceito for D ou E.

os 5Qs 
duas notas bimestrais de uma mesma materia do usuario
devo calcular a media para a atribuição de conceitos 
devo aplicar a atribuição de conceito corretamente 
exibir ao usuario as sequintes informações:
as notas, a média,
o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
ou “REPROVADO” se o conceito for D ou E.
5

nota_1 input "digite a nota 1 da materia x: "
nota_2 input "digite a nota 2 da materia x: "
media = (nota_1 + nota_2) / 2
if media >= 9
print"
    f'o aluna esta com uma media de: {media}\n'
    f'tirou A\n'
    f'esta aprovado!'
" 
elif media >= 75
print"
    f'o aluno esta com a media de: {media}\n'
    f'tirou B\n'
    f'esta aprovado!'
" 
elif media >= 60
print"
    f'o aluno esta com a media de: {media}\n'
    f'tirou C\n'
    f'esta aprovado!' 
"
elif media <= 40
print"
    f'o aluno esta com a media de: {media\n}'
    f'tirou D\n'
    f'esta reprovado!'
" 
else:
print"
    f'o aluno esta com a media de: {media}\n'
    f'tirou E\n'
    f'esta reprovado'
"
"""



nota_1 = float(input('digite a nota 1 da materia x: '))
nota_2 = float(input('digite a mota 2 da materia x: '))
media = (nota_1 + nota_2) / 2 
if media >= 9.0:
    print(
        f'a media do aluno foi de {media}\n'
        f'tirou A\n'
        f'aprovado!'
    )
elif media >= 7.5:
    print(
        f'a media do aluno foi de {media}\n'
        f'tirou B\n'
        f'aprovado!'
    )
elif media >= 6.0:
    print(
        f'a media do aluno foi de {media}\n'
        f'tirou C\n'
        f'aprovado!'
    )
elif media >= 4.0:
    print(
        f'a media do aluno foi de {media}\n'
        f'tiro D\n'
        f'reprovado!'
    )
else:
    print(
        f'a media do aluno foi de {media}\n'
        f'tirou E\n'
        f'reprovado!'
    )
    