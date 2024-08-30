"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o
usuário informe um valor válido.

os 5Qs 

pedir uma nota entre 0 e 10

monstrar uma mensagem caso o valor seja invalido e continuar 
pedindo ate que o usuario informe um valor valido

o programa nao deve finalizar ate que o usuario digite um valor de 0 a 10]

que o usuario acerte a nota 


"""


# jeito meu usando apenas um input 

acerto = False

while acerto == False:  # laço while com uma condição booleano
    numero_usuario = int(input('Digite um nota de 0 a 10: '))
#   if da restrição do problema 
    if numero_usuario < 0 or numero_usuario > 10:
        print('Nota invalida.')
        print('Tente novamente!')
    else: # caso a restrição nao seja ativa quebra do loop
        print('nota valida')
        break

"""
# gabarito da atividade
nota = float(input("Digite uma nota de 0 a 10: ")) # 1º input 
while nota > 10 or nota < 0: # laço while com uma condição 
    nota = float(input("Valor Inválido\nDigite uma nota de 0 a 10: "))
    # 2ª input, junto com o input
"""