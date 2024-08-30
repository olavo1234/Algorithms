"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:

    comprar apenas latas de 18 litros;
    
    comprar apenas galões de 3,6 litros;
    
    misturar latas e galões, de forma que o preço seja o menor.
        
        Acrescente 10% de folga e sempre arredonde os valores para cima,
        isto é, considere latas cheias

        
passos:

o programa deve pedir o tamanho da area a ser pintada
a lata é de 18 litros 1 litro para cada 6 metros que custa 80 reais 
ou em galoes de 3,6 litros que custam 25 reais

imformar ao ususario a quantidade de tinta a serem compradas 
e os preços em 3 sequintes situaçoes 

apenas latas de tintas calculo:
a conta é (18 litros * 6 metros / pela area) para achar a quantidade de latas 
e para ter o preço total é preciso a quantidade de lata para achar o valor total (quantidade de lata * 80 reais) 
sempre fazendo o ceil 

apenas galões calculo:
a conta é (3,6 litros * 6 metros / pela area) para achar a quantidade de galões 
e para ter o preço total e preciso a quantidade de galões para achar o valor total (quantiade de galões * 25 reais)
sempre fazendo o ceil
 
para ter a folga de 10% e preciso multiplicar a area do usuario por 10 

para achar o numero de latas para pintar e misturar com o galão e achar o melhor valor:

FLOOR para colocar o galão se o usuario nao tiver o dinheiro suficiente o sistema mosntra a tinta com o valor mais baixo
pegar a multiplicaçao por 10 da area e dividi pela o rendimento de metros da lata

para achar o numero de galões para pintar e misturar com a lata e achar o menor valor é:

ceil para ter sempre os galões cheias ja que ele é o menor valor de tinta que o usuario pode comprar
pegar a multiplicaçao por 10 da area e separar o (resto) do rendimento de metros da lata e dividir pelo rendimento de metros do galão para ver se da para economizar comprando o recipiente  mais em conta para o usuario

para exibir as informaçoes do usuario na tela usuario é preciso de 3 situaçoes 

com um print exibir:
1 as informaçoes da contidade de latas e seu preço
2 as informaçoes da contidade de galões e seu preço
3 as informaçoes da coontidade de latas e galões e exibir e calcular dentro do print a soma dos dois valores e exibir 
"""

import math

metros_quadrados = float(input('digite os metros quadrados: '))
metros_quadrados_mais_dez = metros_quadrados * 1.0

rendimento_litro = 6

litros_lata = 18
preco_lata = 80
rendimento_lata = rendimento_litro * litros_lata

litros_galao = 3.6
preco_galao = 25
rendimento_galao = rendimento_litro * litros_galao

somente_latas = math.ceil(metros_quadrados / rendimento_lata)
somente_galoes = math.ceil(metros_quadrados / rendimento_galao)
latas = math.floor(metros_quadrados_mais_dez / rendimento_lata)
galoes = math.ceil(
    (metros_quadrados_mais_dez % rendimento_lata) / rendimento_galao
    )

print(
    f"Somente Latas: {somente_latas}, "
    f"custando R${somente_latas * preco_lata}\n"
    f"Somente Galões: {somente_galoes}, "
    f"custando R${somente_galoes * preco_galao}\n"
    f"Latas: {latas} , Galões: {galoes}, "
    f"custando R${((latas * preco_lata) + (galoes *preco_galao)):.2f}"
)