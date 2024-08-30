"""
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem
altura inferior à média de altura desses alunos.
"""

idades = list()
alturas = list()
abaixo_da_media = 0
print('=*'*10)
for i in range(0, 30):
    idades.append(int(input('idade: ')))
    alturas.append(float(input('altura: ')))
    print('=*'*10)
media = sum(alturas) / 30
for idade in idades:
    for altura in alturas:
        if idade >= 13 and altura < media:
            abaixo_da_media =+ 1

print(
    f'A média das alturas foi de {media}.'
    f'\nA quantidade de alunos com mais de' 
    f'\n13 anos e altura inferior a media é {abaixo_da_media}.'
)
