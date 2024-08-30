"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.

os 5Qs
um nummero do usuario inteiro ou decimal

devo analisar se for decimal informa ao usuario e o mesmo se for inteiro

um numero decimal é um numero quebrado

se for decimal ou inteiro informar ao usuario 

5 pseudocodigo

import math

input"digite um numero decimal ou inteiro:"
arredon = math.floor(num)

if arredon == num:
    print"o numero é inteiro"
else:
    print"o numero é decimal"
"""



import math

num = float(input('digite um numero inteiro ou decimal: '))
arredon = math.floor(num)# para arredondar um numero para baixo
# se o numero nao for arredondado(floor para baixo) ele é inteiro
if arredon == num: # se o numero digitado for iqual ao floor ele é um numero inteiro 
    print(f'O numero {num:,.0f} é inteiro')
else:
    print(f'O numero {num:,.2f} é decimal')  

