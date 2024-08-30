"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante :
        aumento de 5% Após o aumento ser realizado,
    informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.

passos
ler e entender o que se esta sendo pedido

receber o salario de um colaborador 

reajustar sequindos os criterios descritos, baseado no salario atual 

salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante :
        aumento de 5% Após o aumento ser realizado,

e exibir na tela do usuario as sequintes mensagens:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
    
os 5Qs 
o salario do usuario 

calcular as porcentagem certa em cada criterio e imprimir o salario antes do reajuste;
a porcentual do aumento aplicado;
o valor do aumento; 
o novo salario, apos o aumento.

so calcular nas porcentagen certa;
imprimir as mensagens certas 

e exibir na tela do usuario as sequintes mensagens:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
5

salario input"salrio"

aumento_20 salario * 20 / 100
aumento_15 salario * 15 / 100
aumento_10 salario * 10 / 100
aumento_5 salario * 5 / 100

if salario <= 280
print(
f'o salario anterior é de {salario}\n'
f'o porcentual do aumento é de 20%\n'
f'o valor do aumento é de {(salario_20 - salario)}\n'
f'o salario apos o aumento é de {salario_20}'
)
elif salario > 280 and salario <= 700
print(
f'o salario anterior é de {salario}\n'
f'o porcentual do aumento é de 15%\n''
f'o valor do aumento é de {(salario_15 - salario)}\n'
f'o salario apos o aumento é de {salario_15}'
)
elif salario > 700 and salario <= 1500
print(
f'o salario anterior é de {salario}\n'
f'o porcentual do aumento é de 10%\n'
f'o valor do aumento é de {(salario_10 - salario)}\n'
f'o salario apos o aumento é de {salario_10}'
)
elif salario >= 1500
print(
f'o salario anterior é de {salario}\n'
f'o porcentual do aumento é de 5%\nb'
f'o valor do aumento é de {(salario_5 - salario)}\n'
f'o salario apos o aumento é de {salario_5}'
)
"""

salario = float(input('informe seu salario atual: '))

aumento_20 = (salario * 20) / 100
aumento_15 = (salario * 15) / 100
aumento_10 = (salario * 10) / 100
aumento_5 = (salario * 5) / 100

if salario <= 280:
 print(
    f'o salario anterior é de R${salario:,.2f}\n'
    f'o porcentual do aumento é de 20%\n'
    f'o valor do aumento é de R$ {aumento_20:,.2f}\n'
    f'o salario apos o aumento é de R${(salario + aumento_20):,.2f}'
)
elif salario > 280 and salario <= 700:
 print(
    f'o salario anterior é de R${salario:,.2f}\n'
    f'o porcentual do aumento é de 15%\n'
    f'o valor do aumento é de R${aumento_15:,.2f}\n'
    f'o salario apos o aumento é de R${(salario + aumento_15):,.2f}'
)
elif salario > 700 and salario <= 1500:
 print(
    f'o salario anterior é de R${salario:,.2f}\n'
    f'o porcentual do aumento é de 10%\n'
    f'o valor do aumento é de R${aumento_10:,.2f}\n'
    f'o salario apos o aumento é de R${(salario + aumento_10):,.2f}'
)
elif salario >= 1500:
 print(
    f'o salario anterior é de R${salario:,.2f}\n'
    f'o porcentual do aumento é de 5%\n'
    f'o valor do aumento é de R${aumento_5:,.2f}\n'
    f'o salario apos o aumento é de R${(salario + aumento_5):,.2f}'
)
