"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.

passos
ler e entender o que se esta sendo pedido
pedir um numero ao usuario
analisar o numero e exibir e sequindo os sequintes criterios 
1 - domingo
2 - segunda
3 - terça
4 - quarta
5 - quinta
6 - sexta
7 - sabado
numero fora esses - valor invalido
os 5Qs
un numero do usuario correspondende a dia da semana 
ler o numero do usuario
se o numero do usuario nao tiver nos criterios exibir "valor invalido"
exibir o dia da semana correspondente 
5

num input "digite un numero correspondente ao dia da semana " 
if num == "1"
print('domingo')
elif num == "2"
print('segunda')
elif num == "3"
print('terça')
elif num == "4"
print('quarta')
elif num == "5"
print('quinta')
elif num == "6"
print('sexta')
elif num == "7"
print('sabado')
else
print('valor invalido!!') 
"""


num = int(input('digite un numero correspondente ao dia da semana: ')) 

if num == "1":
    print('domingo!')
elif num == "2":
    print('segunda!')
elif num == "3":
    print('terça!')
elif num == "4":
    print('quarta!')
elif num == "5":
    print('quinta!')
elif num == "6":
    print('sexta!')
elif num == "7":
    print('sabado!')
else:
    print('valor invalido!') 