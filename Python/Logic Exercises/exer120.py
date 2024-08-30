# meu jeito

# from random import randint
# print("|ACERTE O CHUTE!|")
# print("Eu sou o seu computador e estou aqui para um desafio!!\nTente adivinhar o numero que eu pensar...")
# print("~"*50)
# computador = randint(0,10)
# erro = True
# palp = 1
# escolha = int(input("Digite um numero de 0 a 10: "))
# while erro:
#     if escolha != computador:
#         print("HAHAHA!! Voce errou, tente novemente!!")
#         escolha = int(input("Digite um numero de 0 a 10: "))
#         palp += 1
#     if escolha == computador:
#         print(f"PARABENS!!, voce acertou o chute precisou de {palp} tentativas")
#         erro = False








# forma usando o not para não colocar 2 input no codigo
from random import randint
computador = randint(0,10)
print('eu sou seu computador... acabei de pensar em um numero de 0 a 10')
print('será que voce conseque adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual foi o seu palpite?  '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAiS... Tente mais uma vez')
        else:
            print("MENOS... Tente mais uma vez")
print(f"Acertou com {palpites} tentativas, parabéns!")
