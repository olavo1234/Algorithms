'''
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.

passos
ler o que se esta sendo pedido e entemder
pedir o tamanho em metros quadrados da area a ser pintada 
considerar que a cobertura é de 1 litro para cada 3 metros quadrados 
tinta e vendida em latas de 18 litros, que custam 80 reais 
em uma lata de tinta de 18 litros ela cobre 54 metros cada lata custa 80 reais 
para achar a quantidades de latas de tintas devo pegar o valor total de 18 litros que é 54 e dividir pela informaçao do usuario
e para achar o preço total e so pegar o preço de cada lata e multiplicar pela quantidade de latas de tinta 
depois exibir o resultado daa operaçoes 

os 5Qs 
pedir o tamanho em metros quadrados da area a ser pintada 
devo calcular o total de mertros que tem em uma lata de 18 litros e dividir com os metros quadrados do usuario 
e depois multiplicar com a quantidades de latas do usuario
Informe ao usuário a quantidades de latas de tintaa serem compradas e o preço total.
5

import math

area input "digite o tamanho em metros quadrados para ser pintada "
latas math.ceil"area / 54"
total "latas * 80"
print"total"

'''

import math 

area = float(input('digite é o tamnho em metros quadrados da area a ser pintada: '))
latas = math.ceil(area / 54)
total = latas * 80
print(f'a quantidade de latas que é preciso e de {latas:.0f} e valor total é de R${total:.2f}')

