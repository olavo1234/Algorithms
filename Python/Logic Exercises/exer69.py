"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa
deverá verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e
maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
média calculada.
"""

# não utoizando um valor previo de pessoas
faixetaria = ''
total = 0
cont = 0
continuar = 'S' 
while continuar == 'S':
    n = float(input('Digite a idade dos alunxs: '))
    cont += 1
    total += n
    media = total / cont
    continuar= str(input('Diigte [S/N] para continuar: ')).upper()[0]
if media < 25:
    faixetaria = 'joven'
elif media < 60:
    faixetaria = 'adulta'
elif media > 60:
    faixetaria = 'idosa'
print(
    f'A turma é {faixetaria}'
)




# utilizando um valor previo de pessoas
numero_de_pessoas = int(input("Digite o numero de pessoas: "))
media = 0

# + 1 pois a contagem está iniciando em 1, e não em 0 (o padrão)
for i in range(1, numero_de_pessoas + 1):
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    media = ((media * (i - 1)) + idade) / i

if media < 26:
    print("A turma é jovem")
elif media < 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")
