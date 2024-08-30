"""
Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele mesmo
e por 1.
"""


# n = int(input('Digite um numero: ')) 
# tot = 0
# for c in range(1,n+1):
#     if n % c == 0:
#         tot += 1
#         print(f'Foi divisivel por {c}')
# print(f'O numero {n} foi divisivel {tot} vezes')
# if tot == 2:
#     print('É um numero primo')
# else:
#     print('Não é um numero primo')


# gabarito
numero = int(input("Digite um numero inteiro: "))
primo = True# varivel primo recebe um valor booleano de True
for i in range(2, numero):# laço for que ira contar de 2 ate o numero anterior ao do usuario
    if numero % i == 0:# ver se é divisivel pelos numero acima de 1 e abaixo do numero do ususario
        primo = False# declarar primo como falso se for divisivel
        print(f"{numero} não é primo!")# resultado
        break# quebra do laço for

if primo:# separar os resultados
    print(f"{numero} é primo!")
