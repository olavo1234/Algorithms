"""
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    o produto do (dobro do primeiro com metade do segundo.)
    a soma do (triplo do primeiro com o terceiro.)
    o terceiro elevado ao cubo.

passos 
ler e entender o que  se esta sendo pedido
pedir ao usuario 2 numeros inteiros e 1 real 
gravar os numeros em variaves em lista
calcular o (index 0 x2) * (index 1 / 2)
quarda em uma variavel 
exibir 
calcular o (index 0 x30) + (index 2)
exibir 
calcular o ((index 2)**3)
exibir 

so 5Qs
2 números inteiros e um número real.

o produto do (dobro do primeiro com metade do segundo.)
a soma do (triplo do priomeiro com o terceiro.)
o terceiro elevado ao cubo.

devo fazer as operaçaes somente com os numeroa do usuario

alcule e mostre:
   o produto do (dobro do primeiro com metade do segundo.)
    a soma do (triplo do primeiro com o terceiro.)
    o terceiro elevado ao cubo.

5 pseudocodigo

num1 input"digite o primeiro mumero inteiro"
num2 input"digite o segundo numero inteiro"
num3 input"gigite um numero real: "
lista[num1, num2, num3]
cal1 ((lista[0] * 2)) * ((lista[1]) / 2)
print(cal1)
cal2 ((lista[o]) * 3) + (lista[2])
print(cal2)
cal3 ((lista[2])**3)
print(cal3)
"""

num1 = int(input('digite o primeiro mumero inteiro: '))
num2 = int(input('digite o segundo numero inteiro: '))
num3 = float(input('gigite um numero real: '))
lista = [num1, num2, num3]
cal1 = ((lista[0])*2) * ((lista[1])/2)
print(f'o produto do dobro do primeiro com metade do segundo é {cal1:,}')
cal2 = ((lista[0]*3)) + (lista[2])
print(f'a soma do triplo do primeiro com o terceiro é {cal2:,}')
cal3 = ((lista[2]**3))
print(f'o terceiro elevado ao cubo é {cal3:,}')
