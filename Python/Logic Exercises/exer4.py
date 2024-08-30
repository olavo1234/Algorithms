'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.

paços 
1 pedir as 4 notas bimestrais
2 criar uma variavel "MEDIA"
3 somar elas e dividir pelo numero de notas  
4 exibir na tela a media do aluno 

os 5Qs
as 4 notas 
somar e dividir pelo numero de notas que no caso e 4
tem que ser somente 4 notas 
exibir a media do aluno

nota_1 = input ('digite a primeira nota: ')
nota_2 = input ('digite a segunda nota: ')
nota_3 = input ('digite a terceira nota: ')
nota_4 = input ('digite a quarta nota: ')

media = nota_1 + nota_2 + nota_3 + nota_4
media = media \ 4
    print(media)

'''

nota_1 = int(input ('digite a primeira nota: '))
nota_2 = int(input ('digite a segunda nota: '))
nota_3 = int(input ('digite a terceira nota: '))
nota_4 = int(input ('digite a quarta nota: '))
media =  (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(
f'a media das notas {nota_1:.2f}, {nota_2:.2f},'
f' {nota_3:.2f} e {nota_4:.2f} é {media:.2f}'
)
