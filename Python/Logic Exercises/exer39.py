"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).


os 5Qs 
um numero do usuario

devo tirar o resto por dois (se) o resultado der 0 o numero é par 
e para impar quando dividimos por 2 e seu resultado der diferente de 0 

se o numero se for 0 é par e se dar diferente de 0 é impar

monstrar se o numero é par e impar

pseudocodigo

numero int input"digite um numero inteiro: "
par numero % 2 
impar numero % 2

if par == 0:
 print"o numero {numero:.0f} é par"
else:
 print"o numero {numero:.0f} é impar"
"""


#Consideramos um número como sendo par quando o dividimos
#por dois e seu resto é zero. Já um número é ímpar quando
#na divisão por dois, o resto é diferente de zero. 
numero = int(input('digite um numero inteiro: '))
resultado = numero % 2

if resultado == 0:
    print(f'o numero {numero:.0f} é par')
else:
    print(f'o numero {numero:.0f} é impar') 


#           o codigo podia ser mais curto

'''
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")
'''
