"""
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
    equilátero, isósceles ou escaleno.

Dicas:
    Três lados formam um triângulo quando a soma de
        quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
passos 
ler e entender oque se esta sendo pedido
pedir os valores de tres lados do triangulo
informa para o usuario se o valores podem ser um treangulo ou nao 
para ser um triangulo a soma dos dois lados tem que ser maior que o terceiro
depois disso indicar caso os lados formen o triangulo se é:
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
os 5Qs 
tres valores do usuario 
para ser um triangulo a soma dos dois lados tem que ser maior que o terceiro
depois disso indicar quais os lados formen o triangulo
indicar corretamnete quais o lados que forman o triangulo
exibir os valores forman o triangulo e exibir corretamante as sequintes informações:
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
5
val1 input"informe o 1º valor: "
val2 input"informer o 2º valor: "
val3 input"informe o 3º valor: " 
triangulo = val1 + val2
if triangulo > val3
print('é um triangulo')
else:
print('nao é um triangulo')

if  val1 == val2 == val3
print('triangulo iquilatero)
elif val1 == val2 or val2 == val1 or val3 == val1 or val3 == val2 or val2 == val3:
print('triangulo isosceles')
else:
print('triangulo escaleno')

"""






#        nao é possivel!!
'''
val1 = int(input('informe o 1º valor: '))
val2 = int(input('informer o 2º valor: '))
val3 = int(input('informe o 3º valor: ')) 
triangulo = val1 + val2
if triangulo > val3:
    print('forma um triangulo')
else:
    print('nao forma triangulo')

if val1 == val2 == val3:
    print('é um triangulo iquilatero')
elif val1 == val2 or val2 == val1 or val3 == val1 or val3 == val2 or val2 == val3:
    print('é um triangulo isosceles')
else:
    print('é um triangulo escaleno')

'''


#        o que esse cara fez????????

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if (
    (lado1 + lado2 > lado3)
    and (lado1 + lado3 > lado2)
    and (lado2 + lado3 > lado1)
):
    if (lado1 == lado2) and (lado2 == lado3):
        print("É um triângulo equilátero!")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("É um triângulo isósceles!")
    else:
        print("É um triângulo escaleno!")
else:
    print("Não é um triângulo!")


