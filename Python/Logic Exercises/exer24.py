"""
Faça um Programa que leia três números e mostre o maior deles.

passos 
ler e entender o que se esta sendo pedido
pedir tres numeros ao usuario
quardar os tres numeros em variaveis
fazer a comparaçao deles
exibir o maior numero para o usuario 

os 5Qs 
três números
mostre o maior deles
somente sera de tres numeros 
Faça um Programa que leia três números e mostre o maior deles.
5

n1 = input"informe o primeiro numero"
n2 = input"informe o segundo numero"
n3 = input"informe o terceiro numero"
if n1 > n2 or n1 > n3
print"{n1}"
elif n2 > n1 or n2 > n3 
print"{n2}"
else:
print"{n3}"

"""

#   abrir mais a mente na resoluçao de um problema

'''
n1 = int(input('informe o primeiro numero: '))
n2 = int(input('informe o segundo numero: '))
n3 = int(input('informe o terceiro numero: '))
if n1 > n2:
    print(F'{n1}')
elif n2 > n1:
    print(F'{n2}')
else: 
    print(f'{n3}')

'''


numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))
numero3 = float(input("Digite mais um numero: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} foi o maior numero digitado.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} foi o maior numero digitado.")
else:
    print(f"{numero3} foi o maior numero digitado.")
