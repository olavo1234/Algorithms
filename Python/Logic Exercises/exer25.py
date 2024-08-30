"""
Faça um Programa que leia três números e mostre o maior e o menor deles.

passos
ler e entender o que se esta sendo pedido
pedir 3 numros ao usuario 
n1,n2,n3
gravar eles em uma variavel
para exibir tera que ser apenas um print
comparar os seus valores com o if e o and
e o principal.

DEIXA O PAI COZINHAR!!!!! 

"""

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
numero3 = int(input("Digite mais um numero: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} foi o maior numero digitado")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} foi o maior numero digitado")
elif numero3: 
    print(f"{numero3} foi o maior numero digitado")

if numero1 < numero2 and numero1 < numero3:
    print(f'{numero1} foi o menor digitado ')
elif numero2 < numero1 and numero2 < numero3:
    print(f'{numero2} foi o menor digitado')
else:
    print(f'{numero3} foi o menor digitado')
