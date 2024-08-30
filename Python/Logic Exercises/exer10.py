"""
Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit.

passos
pesquisar a formula de conversao e entendela
mentalizar e transforma la em codigo 
pedi uma temperatura em celsius 
gravar ela em uma varivel 
declarar uma variavel chamada de fahrenheit
fazer o calculo que converte a temperatura

os 5Q
uma temperatura em graus celsius 
devo colocar ele em uma formula 
devo fazer a conversao da maneira correta
a conversao de celsius para fahrenheit
5

c = input"informe a temperatura em celsius: "
f = (C * 1.8) + 32
print"f"
"""

c = float(input('informe a temperatura em graus celsius: '))
f = (c * 1.8) + 32
print(f'a temperatura de {c:.1f}ºC em fahrenheit é {f:.1f}')
