"""
Faça um Programa que peça um número correspondente a um determinado ano e em
seguida informe se este ano é ou não bissexto.

passos 
ler e entender o que se esta sendo pedido
pedir a usuario informa um numero correspondente a um ano
para calcular um ano bissexto é necessario pegar a ultima dezena do ano e dividir por 4 
o ano e bissexto somente se for divisivel por 4 se o ano terminar com 00 dividir por 400
informa ao usuario se o ano é ou nao bissexto

os 5Qs 
um valor de determinado ano 
calcular para ver se é um ano bissexto sempre dividir por 4
se o ano terminar com 00 dividir por 400
informa ao usuario se o ano é bissexto ou nao

"""

#   falha no codigo por causa do calculo 
#   e das operaçoes do python


ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print(f"{ano} é bissexto!")
else:
    print(f"{ano} não é bissexto!")


