"""
Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.

passos
ler e entender o que se esta sendo pedido
pedir o preço de tres produtos
informa qual produto se deve comprar com base no mais barato
gravar os preços em uma variavel 
comparar usando o and para achar o mais barato
exibir o produto mais barato para o usuario

os 5Qs
preço de tres produtos
informa qual produto se deve comprar 
nao informar produtos caros 
informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.
5  

n1 input"informe o primeiro preço"
n2 input"informe o segundo preço"
n3 input"informe o terceiro preço"
if n1 < n2 and n1 < n3
print"voce devera pagar {n1}"
elif n2 < n1 and n2 < n3 
print"voce devera pagar {n2}"
else
print"voce devera pagar {n3}"
"""

'''
v1 = float(input('informe o primeiro valor: '))
v2 = float(input('informe o segundo valor: '))
v3 = float(input('informe o terceiro valor: '))
if v1 < v2 and v1 < v3:
    print(f'voce deve comprar com o valor de R${v1:.2f}')
elif v2 < v1 and v2 < v3:
    print(f'voce deve comprar com o valor de R${v2:.2f}')
elif v3 < v1 and v3 < v2:
    print(f'voce deve comprar com o valor de R${v3:.2f}') 
elif v1 == 0 and v2 == 0 and v3 == 0:
    print("valor invalido!!")

'''

#   prestar mais atençao no que se esta sendo pedido


preco1 = float(input("Digite o preço do produto 1: "))
preco2 = float(input("Digite o preço do produto 2: "))
preco3 = float(input("Digite o preço do produto 3: "))
if preco1 < preco2 and preco1 < preco3:
    print(f"O produto com o menor preco é o 1, custando R${preco1:.2f}")
elif preco2 < preco1 and preco2 < preco3:
    print(f"O produto com o menor preco é o 2, custando R${preco2:.2f}")
else:
    print(f"O produto com o menor preco é o 3, custando R${preco3:.2f}")


    