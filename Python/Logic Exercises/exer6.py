'''
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

lembrar da formula da conta
fazer os passos corretop do codigo 
pedir ao usuario o raio do circulo
colocar o valor "pi" em uma variavel constante
fazer a formula de vezes calculando ("raio vezes pi 3,14 e") e marcar em uma variavel
exibir na tela 

os 5Qs 
o raio e o valor de pi
multiplicar os dois e exibir o valor 
nao pode calcular nenhum outro valor a nao ser esses 
exebir a area do circulo 

raio = float(input('digite o valor do raio: '))
pi = 3,14
area = raio * pi
print(f'o valor da area é {area:.2f}')

'''

pi = 3.1415926
raio = float(input('digite o valor do raio: '))
area = (raio ** 2) * pi
print(f'o valor da area é {area:,.2f}')
