"""
Faça um programa que calcule o valor total investido por um colecionador em sua
coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""


soma = 0
quantidade_cds = int(input('Digite a quantidade total de CDs: '))
for c in range(1,quantidade_cds+1):
    preco_cds = float(input(f'Informe o preço do CD {c}: '))
    soma += preco_cds
media_valor = soma / quantidade_cds
print(
    f'O total investido na coleção é de R${soma:,.2f} reias'
    f'\nÉ a média de cada um é de R${media_valor:,.2f} reais'
)



# forma mais curta
cds = int(input("Digite a quantidade de CDs: "))
preco = 0
for i in range(cds):
    preco += float(input(f"Digite o preço do CD {i+1}: "))
print(f"Preço total: R${preco:.2f}\nMédia de custo por CD: R${preco/cds:.2f}")

