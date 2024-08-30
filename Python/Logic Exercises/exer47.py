"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.

os 5Qs

o nome do usuario e a senha 

devo pedir o nome do usuario e a senha 

nao aceitar a senha iqual ao nome do usuario 

monstrar uma mensagem se erro e voltar a pedir as informações 

"""



# codigp longo
incorreto = True
while incorreto == True:
    nome_usuario = str(input('Digite o nome do usuario: '))
    senha = input('Digite sua senha: ')
    
    if nome_usuario == senha:
        print('Nome de usuario nao pode ser igual a senha!')
    else:
        break




# codigo curto
"""
usuario = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")
while usuario == senha:
    print("Nome de usuario nao pode ser igual a senha!")
    usuario = input("Digite o nome de usuario: ")
    senha = input("Digite a senha: ")

"""
