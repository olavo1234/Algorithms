
'''

Faça um Programa que converta metros para centímetros.

passos

estudar a converçao de medidas 
pedir um numero para o usuario 
gravar ele em uma varivel 
fazer a formula
depois gravar a formula do calculo em uma varivel junto com um resultado
exibir o centimetro ja convertido na tela 
#    os 5Qs 
1 um numero em centimetro do usuario para fazer a converçao
2 devo multiplicar po 10 duas ou (fazer por 100) vezes para ter o centimetro
3 nao multiplicar o numero por mais de duas vezes 
4 ter a unidade de centimetro

5 

metros = int(input('digite os metros: '))
centimetro = metro * 100
 print(f'{metro:.2f} equivalem a {centimetro:.2f} centimetros.')
'''

metro = float(input('digite o metro: '))
centimetro = metro * 100
print(f'{metro:.2f} equivalem a {centimetro:.2f} centimetros.')

