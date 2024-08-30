'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS
    quanto pagou ao sindicato
    o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato (5%) : R$
    = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.

passos 
perguntar a o usuario valor hora e o numero de horas trabaladas por mes
quardar em uma variavel 
depois multiplicar valor hora * horas trabalhadas  
depois quardar esse valor em uma variavel 
exibir o salario bruto 
descontar 11% para o inposto de renda, 8% para o inss, 5% para o sindicato
exibir na tela o quanto pago ao:
 + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato (5%) : R$
    = Salário Liquido : R$

os 5Qs 
o valor_hora e horas_trabalhadas 
devo multiplicalos e exibir na tela e descontar 11% para o inposto de renda, 8% para o inss, 5% para o sindicato
devo usar apemas a multiplicaçao e diminuir pela quantidade certa de porcentagem
consequir o total do seu salario no referido mes exibir na tela o quanto pago ao:
 + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato (5%) : R$
    = Salário Liquido : R$
5 pseudocodigo

valor_hora = input"informe o quanto voce quanha por hora
horas_trabalhadas = input"informe o numero de horas trabalhadas no mes"
salario_bruto = valor_hora * horas_trabalhadas 
print"salario_bruto"
ir = (salario_bruto * 11) / 100
print"ir"
inss = (salario_bruto * 8) / 100
print"inss"
sindicato = (salario_bruto * 5) / 100
print"sindicato"
salario_liquido = (salario_bruto - ir) - inss - sindicato
print"salario_liquido"
'''

valor_hora = float(input('informe o quanto voce quanha por hora: '))
horas_trabalhadas = float(input('informe o numero de horas trabalhadas no mes: '))
salario_bruto = valor_hora * horas_trabalhadas
print(f'seu salrio bruto é de R${salario_bruto:.2f}')
IR = (salario_bruto * 11) / 100
print(f'voce pagara de IR: R${IR:.2F} ')
INSS = (salario_bruto * 8) / 100
print(f'voce pagara de INSS: R${INSS:.2F}')
sindicato = (salario_bruto * 5) / 100
print(f'voce pagara de sindicato: R${sindicato:.2f}')
salario_liquido = (salario_bruto - IR) - INSS - sindicato
print(f'seu salario liquido é de R${salario_liquido:.2f} ')

