"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
operação ele deseja realizar.

O resultado da operação deve ser acompanhado de uma
frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.

os 5Qs

pedir dois numeros ao usuario

perguntar ao usuario qual e a operação que ele quer, o resultado da operação
deve ser acompanhada de uma frase que diga se o numero é par ou impar;
positivo ou negativo; inteiro ou decimal

ele é limitado de operações de ate 2 numeros

devo informa o resultado da operação junto com uma frase que diga se o numero 
é par ou impar; positivo ou negativo; inteiro ou decimal

"""

numero_1 = float(input('digite o 1º numero: '))
numero_2 = float(input('digite o 2º numero: '))
operacao = str(input('digite a operação desejada: ')).strip()

soma = numero_1 + numero_2
menos = numero_1 - numero_2
mult = numero_1 * numero_2
div = numero_1 / numero_2

print("-="*25)

if operacao == "soma" or operacao == "adição" or operacao == "adiçao":
    print(f'o resultado da soma é {soma:,.2f}', end=' ')
    print('o numero é par')if soma % 2 == 0 else print('o numero é impar')
    print('o numero é positivo')if soma > 0 else print('o numero é negativo' )
    print('o numero é inteiro')if soma % 1 == 0 else print('o numero é decimal')

elif operacao == "menos" or operacao == "subtração" or operacao == "subtraçao":
    print(f'o resultado da subtração é {menos:,.2f}', end=' ')
    print('o numero é par')if menos % 2 == 0 else print('o numero é impar')
    print('o numero é positivo')if menos > 0 else print('o numero é negativo')
    print('o numero é inteiro')if menos % 1 == 0 else print('o numero é decimal')

elif operacao == "vezes" or operacao == "multiplicação" or operacao == "multiplicaçao":
    print(f'o resultado da multiplicação é {mult:,.2f}', end=' ')
    print('o numero é par')if mult % 2 == 0 else print('o numero é impar')
    print('o numero é positivo')if mult > 0 else print('o numero é negativo')
    print('o numero é inteiro')if mult % 1 == 0 else print('o numero é decimal')

elif operacao == "dividir" or operacao == "divisão" or operacao == "divisao":
    print(f'o resultado da divisão é {div:,.2f}', end=' ')
    print('o numero é par')if div % 2 == 0 else print('o numero é impar')
    print('o numero é positivo')if div > 0 else print('o numero é negativo')
    print('o numero é inteiro')if div % 1 == 0 else print('o numero é decimal')

else:
    print('valor invalido!')

