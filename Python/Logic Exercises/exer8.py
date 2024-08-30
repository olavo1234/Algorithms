'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
passos 
perguntar a o usuario valor hora e o numero de horas trabaladas por mes
quardar em uma variavel 
depois multiplicar valor hora * horas trabalhadas  
depois quardar esse valor em uma variavel 
exibir o resultado ao usuario 

os 5Qs 
o valor_hora e horas_trabalhadas 
devo multiplicalos e exibir na tela
devo usar apemas a multiplicaçao
consequir o total do seu salario no referido mes
5
valor_hora = input"informe o quanto voce quanha por hora"
horas_trabalhadas = input"informe o numero de horas trabalhadas no mes"
salario = valor_hora * horas_trabalhadas 
print(salario)
'''

valor_hora = float(input('informe o quanto voce quanha por hora: '))
horas_trabalhadas = float(input('informe o numero de horas trabalhadas no mes: '))
salario = valor_hora * horas_trabalhadas
print(
    f"Ganhando R${valor_hora:,.2f} a hora, tendo trabalhado "
    f"{horas_trabalhadas} horas no mês, seu salário este mês "
    f"é de R${salario:,.2f}."
)

