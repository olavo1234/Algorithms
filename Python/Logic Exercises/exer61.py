"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120
"""

# forma minha utilizando a maneira de print do exemplo
numero = int(input("Digite um numero: "))
fatorial = numero
for c in range(numero-1, 0, -1): 
    fatorial *= c
print(f'{numero}!:',end="")
ultimo = "1"
for c in range(numero, 1, -1):
    print(c,end=".")
print(ultimo, end="")
print(f' = {fatorial:,.0f}')



# forma do gabarito 
"""
numero = int(input("Digite um numero: "))
fatorial = 1
for i in range(numero, 1, -1):
    fatorial *= i
print(f"O fatorial de {numero} é {fatorial}")
"""


# forma do devaprender
"""
numero = int(input('digite um numero:'))
if numero > 0:
    fatorial = 1
for item in range(1,numero + 1):
    fatorial = fatorial * item 
print(fatorial)
"""