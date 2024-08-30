"""
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax² + bx + c.

O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo
        grau e o programa não deve fazer pedir os demais valores,
        sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raízes reais.
        Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz
        real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais;
        informe-as ao usuário;

passos 
ler e entender o que se esta sendo pedido

o programa devera pedir ao usuario os valores de A / B / C

fazer o calculo da formula para achar o delta

depois disso exibir o valor de delta sequindo as sequintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo
        grau e o programa não deve fazer pedir os demais valores,
        sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raízes reais.
        Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz
        real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais;
        informe-as ao usuário;

os 5Qs 
tres valores do usuario 
devo calcular a equação de 2ª grau
se o valor de delta dor menor que zero encerrar o programa
Se o usuário informar o valor de A igual a zero, a equação não é do segundo
        grau e o programa não deve fazer pedir os demais valores,
        sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raízes reais.
        Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz
        real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais;
        informe-as ao usuário;
5
#            so sair do pseu depois de ter certeza do que leu e escrever

val1 = float(input('digite o valor de A: '))
val2  = float(input('digite o valor de B: '))
val3 = float(input('digite o valor de C: '))
val_b = (val2**2)
val_ac = val1 * val3
delta = val_b -4 * val_ac

if delta < 0
print"a equaçao nao possui raiz"
elif delta == 0 
print "a equaçao tem apenas uma raiz"
else
print"a equaçao possui duas raizes" 
"""




'''
#   usar o reciocinio para exemplificar as utilidades do if e else

val1 = float(input('digite o valor de A: '))
if val1 == 0:
    print('essa equaçao nao é do 2ª grau!!')
else:
 val2  = float(input('digite o valor de B: '))
 val3 = float(input('digite o valor de C: '))
 val_b = (val2**2)
 val_ac = val1 * val3
 delta = val_b -4 * val_ac


 if val1 == 0:
    print('essa equaçao nao é do 2ª grau!!')
 elif delta < 0:
    print('a equaçao nao possui raiz')
 elif delta == 0: 
    print('a equaçao tem apenas uma raiz')
 elif delta > 0:
    print('a equaçao possui duas raizes') 
'''

A = float(input('digite o valor de A: '))
if A == 0:
    print('não é uma equaçao de 2ª grau')
else:
    B = float(input('gigite o valor de B: '))
    C = float(input('digite o valor de C: '))
    delta = (B ** 2) - (4 * A * C)
    if delta < 0:
        print('delta e menor que 0. nao ha raizes')
    elif delta == 0:
        raiz = (-B) / (2 * A)
        print(f'delta é zero a raiz é de {raiz:.2f}')
    else:
        raiz1 = (- B  +  (delta ** (1/2))) / (2 * A) 
        raiz2 = (- B  -  (delta ** (1/2))) / (2 * A)
        print(
            f'delta maior que zero. a raiz 1 é de {raiz1:.2f} e a raiz 2 é {raiz2:.2f}'
        )
    

