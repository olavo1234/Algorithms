'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso
(peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite
e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.

passos 
ler e entender o que se pede 
pergunter os kilos dop peixe e declarar uma variavel chamada peso de peixe
calcular o excesso 
declarar uma variavel excesso a quantidade de kilos alemn do limite
declarar uma variavel chamada multa o valor que joao deverá pagar.
imprimir os dados ma tela

os 5Qs 
da quantidade de kilos do peixe 
devo calcular e ver se passo do excesso de 50 kilos se passo vou somar 4 reais a cada kilo
nao posso permitir que passe de 50 kilos
imprimir os dados com as mensagens adequadas e aplicare o valor da mult que joao ira pagar 

5    psudoodigo

peso_peixe = input('informe os kilos do peixe: ')
if peso_peixe > 50
 print('sua multa e de 4 reais por kilo excedido.')
else
print(voce nao levou multa)

'''


'''
peso_peixe = float(input('informe quantos kilos de peixe voce pegou: '))
if peso_peixe > 50:
    print(f'{peso_peixe:.2f}kg voce excedeu limite de 50 kg, sua multa será de R$ 4,00 por kilo ')
else:
    print(f'voce tem {peso_peixe:.2f} kg menos ou iqual a 50 kg nao levou multa')
'''

#                  pensar melhor nas resoluçoes do poblema 
#                  ter a mente mais aberta para a resoluçao de poblema 
#                  ler com mais atençao

peso = float(input("Digite o peso da pesca em Kg: "))
excesso = peso - 50
multa = excesso * 4
print(f"Foram {excesso:.2f}Kg em excesso, logo, a multa é de R${multa:.2f}.")
                                                