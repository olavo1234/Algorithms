"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita).

O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.

Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00

passos

ler e entender o que se esta sendo pedido 

perguntar ao usuario a quntidades de horas trabalhadas por mes e o valor hora 

multiplicar os valores e achar o salario 

decontar o inss(10%) o fgts(11) 

descontos do IR :

Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

imprimiras sequintes mensagens:

Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00

os 5Qs

o valor hora e horas trabalhadas por mes

devo calcular o o salario liquido do usuario que é salario bruto menos os impostos

devo calcular corretamente os descontos ;
devo exibir as informaçoes corretamente na tela

calcular os descontos do IR: 

Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%
e exibir as sequintes informaçoes;

Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,0

5

valor_hora input"digite o valor hora:  "
horas_trabalhadas_mes input"digite as horas trabalhadas por mes: "
salario_bruto (valor hora * horas_trabalhadas_mes)
inss ((salario * 10) / 100) 
fgts ((salario * 11) / 100)
ir_5 ((salario * 5) / 100)   
ir-10 ((salario * 10) / 100)     
ir_20 ((salario * 20) / 100)    

if salario_bruto <= 900
print(
        f'Salário Bruto:                  : R${salario_bruto}\n'
        f'(-) IR (isento)                 : R$00\n'
        f'(-) INSS ( 10%)                 : R${inss}\n'
        f'FGTS (11%)                      : R${fgts}\n'
        f'Total de descontos              : R${(inss+fgts)}\n'
        f'Salário Liquido                 : R${((salario-fgts)-inss}\n'
)
elif salario_bruto > 900 and salario <= 1500:
print(
             
        f'Salário Bruto:                  : R${salario_bruto}\n'
        f'(-) IR (5%)                     : R${ir_5}\n' 
        f'(-) INSS ( 10%)                 : R${inss}\n'
        f'FGTS (11%)                      : R${fgts}\n'  
        f'Total de descontos              : R${(ir_5+inss+fgts)}\n'  
        f'Salário Liquido                 : R${(salario_bruto-ir_5-inss-fgts)}\n'
)
elif salario_bruto > 1500 and salario <= 2500:
print(
             
        f'Salário Bruto:                  : R${salario_bruto}\n'
        f'(-) IR (10%)                    : R${ir_10}\n' 
        f'(-) INSS ( 10%)                 : R${inss}\n'
        f'FGTS (11%)                      : R${fgts}\n'  
        f'Total de descontos              : R${(ir_10+inss+fgts)}\n'  
        f'Salário Liquido                 : R${(salario_bruto-ir_10-inss-fgts)}\n'
)
elif salario > 2500:
print(

        f'Salário Bruto:                  : R${salario_bruto}\n'
        f'(-) IR (10%)                    : R${ir_20}\n' 
        f'(-) INSS ( 10%)                 : R${inss}\n'
        f'FGTS (11%)                      : R${fgts}\n'  
        f'Total de descontos              : R${(ir_20+inss+fgts)}\n'  
        f'Salário Liquido                 : R${(salario_bruto-ir_20-inss-fgts)}\n'
)
"""





valor_hora = float(input('digite o valor hora: '))
horas_trabalhadas_mes = float(input('digite as horas trabalhadas por mes: '))
salario_bruto = (valor_hora * horas_trabalhadas_mes)

inss = ((salario_bruto * 10) / 100) 
fgts = ((salario_bruto * 11) / 100)
ir_5 = ((salario_bruto * 5) / 100)   
ir_10 = ((salario_bruto * 10) / 100)     
ir_20 = ((salario_bruto * 20) / 100)    

if salario_bruto <= 900:
 print(
        f'Salário Bruto:                  : R${salario_bruto:,.2f}\n'
        f'(-) IR (isento)                 : R$00\n'
        f'(-) INSS ( 10%)                 : R${inss:,.2f}\n'
        f'FGTS (11%)                      : R${fgts:,.2f}\n'
        f'Total de descontos              : R${inss:,.2f}\n'
        f'Salário Liquido                 : R${(salario_bruto-inss):,.2f}\n'
)
elif salario_bruto > 900 and salario_bruto <= 1500:
 print(
             
        f'Salário Bruto:                  : R${salario_bruto:,.2f}\n'
        f'(-) IR (5%)                     : R${ir_5:,.2f}\n' 
        f'(-) INSS ( 10%)                 : R${inss:,.2f}\n'
        f'FGTS (11%)                      : R${fgts:,.2f}\n'  
        f'Total de descontos              : R${(ir_5+inss):,.2f}\n'  
        f'Salário Liquido                 : R${(salario_bruto-ir_5-inss):,.2f}\n'
)
elif salario_bruto > 1500 and salario_bruto <= 2500:
 print(
             
        f'Salário Bruto:                  : R${salario_bruto:,.2f}\n'
        f'(-) IR (10%)                    : R${ir_10:,.2f}\n' 
        f'(-) INSS ( 10%)                 : R${inss:,.2f}\n'
        f'FGTS (11%)                      : R${fgts:,.2f}\n'  
        f'Total de descontos              : R${(ir_10+inss):,.2f}\n'  
        f'Salário Liquido                 : R${(salario_bruto-ir_10-inss):,.2f}\n'
)
elif salario_bruto > 2500:
 print(

        f'Salário Bruto:                  : R${salario_bruto:,.2f}\n'
        f'(-) IR (10%)                    : R${ir_20:,.2f}\n' 
        f'(-) INSS ( 10%)                 : R${inss:,.2f}\n'
        f'FGTS (11%)                      : R${fgts:,.2f}\n'  
        f'Total de descontos              : R${(ir_20+inss):,.2f}\n'  
        f'Salário Liquido                 : R${(salario_bruto-ir_20-inss):,.2f}\n'
)