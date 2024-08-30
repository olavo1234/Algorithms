"""
Faça um Programa que peça um valor e mostre na tela se o valor é
positivo ou negativo.

passos
pedir um valor ao usuario 
comparar se o valor e maior ou menor que 0 
se for maior exibir na tela o valor é positivo 
se for menor exibir na tela o valor é negativo

os 5Qs 
um valor do usuario
caomparar ele com zero e ver se é maior positivo ou menor negativo
ter apenas um valor
mostrar na tela se o valor e positivo ou negativo
5

float input"digite um valor: "
if numero > 0 
print"o valor é positivo"
else 
print"o valor é negativo"
"""

numero = float(input('informe um numero: '))
if numero >= 0:
    print(f'o numero {numero:.0f} é positivo!')
else:
    print(f'o numero {numero:.0f} é negativo!')
