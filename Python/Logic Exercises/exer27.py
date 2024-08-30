"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.

passos 

ler e entender o que se esta sendo pedido 
pedir tres numeros ao usuario 
comparalos e monstrar em ordem decrescente (do maior para o menor)
exibir a ordem para o usuario  

os 5Qs 
3 numeros do usuario
monstralos em ordem decrescente
devo mostralo na ordem certa
exibir os 3 numeros em ordem decrescente
5
n1 input"digite o primeiro numero: " 
n2 input"digite o segundo numero: " 
n3 input"digite o terceiro numero: "

if n1 > n2 and n1 > n3
print"n1"

if n2 > n1 and n2 > n3 
print"n2"

if n3 > n1 snd n3 > n2
print"n3"

"""

#  ERRADO

'''

n1 = int(input('didite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print(f'{n1}')

if n2 > n1 and n2 > n3: 
    print(f'{n2}')

if n3 > n1 and n3 > n2:
    print(f'{n3}')

'''

#  CERTO

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
numero3 = int(input("Digite mais um numero: "))
if numero1 > numero2 > numero3:
    print(numero1, numero2, numero3)
elif numero1 > numero3 > numero2:
    print(numero1, numero3, numero2)
elif numero2 > numero1 > numero3:
    print(numero2, numero1, numero3)
elif numero2 > numero3 > numero1:
    print(numero2, numero3, numero1)
elif numero3 > numero1 > numero2:
    print(numero3, numero1, numero2)
else:
    print(numero3, numero2, numero1)
