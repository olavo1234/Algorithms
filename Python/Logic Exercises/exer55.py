"""
Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.
"""

comeco = int(input("digite um numero inteiro para iniciar: "))
fim = int(input("digite um numero inteiro para finalizar: ")) 
for n in range(comeco +1, fim):# deconsiderar os numeros digitados e colocar os numero entre eles
    print(n)


