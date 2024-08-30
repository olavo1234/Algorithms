"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

passos

fazer o usuario escrever o seu genero com "f" e "m"
fazer letra escrever F - Feminino, M - Masculino, outra letra - Sexo Inválido

os 5Qs
verificar se a letra digitada é "f" ou "m" 
letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
as letras deve conter corretamente as informaçoes 
fazer a letra escrever F - Feminino, M - Masculino, outra letra - Sexo Inválido
5 

input"digite "M" se voce é do genero masculino ou "f" se for feminino: "
if masculino == "m" or masculino == "M":
print"masculino"
elif feminino == "f" or feminino == "F":
print"feminino"
else:
print"sexo invalido" 
"""

sexo = input('digite "M" se voce é do genero masculino ou "f" se for feminino: ')
if sexo == "m" or sexo == "M":
    print('masculino')
elif sexo == "f" or sexo == "F":
    print('feminino')
else:
    print('sexo invalido')