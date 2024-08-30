'''
passos 
1 ler e emtender o que se esta sendo pedido 
2 pedir o valor do lado do quadrado do usuario
3 gravar em uma variavel 
4 calcular a pontecializaçao por 2 desse valor 
5 gravar em uma variavel
6 depois calcular o dobro da area e monstrar ao usuario

os 5Qs
o valor do lado do quadrado
elevar a o quadrado e depois multiplicar por dois
eu devo monstrar ao o usuario apenas o doblo da area
que imprima na tela o doblo da area do quadrado
5
lado = input"digite o valor do lado do quadrado"
areax2 = (lado**2) * 2
print"areax2
'''

lado = float(input('digite o valor do lado do quadrado: '))
areax2 = (lado**2) * 2
print(f"O dobro da área de um quadrado de lado {lado:,.2f}m é {areax2:,.2f}m²")
