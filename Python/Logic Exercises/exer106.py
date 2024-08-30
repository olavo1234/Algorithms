"""
Utilize uma lista para resolver o problema a seguir.
Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas
daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe
$200 mais 9 por cento de $3000, ou seja, um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos
vendedores receberam salários nos seguintes intervalos de valores:
    # $200 - $299
    # $300 - $399
    # $400 - $499
    # $500 - $599
    # $600 - $699
    # $700 - $799
    # $800 - $899
    # $900 - $999
    # $1000 em diante
Desafio:
    # Crie uma fórmula para chegar na posição da lista a partir do salário,
    # sem fazer vários ifs aninhados.
"""



limites = [
    200, 299,
    300, 399,
    400, 499,
    500, 599,
    600, 699,
    700, 799,
    800, 899,
    900, 999,
    1000
]
porcentagem = 9
cont = 0 

salario = float(input('Informe o seu salário: R$'))
vendas_brutas = float(input('Digite o valor da suas vendas brutas: R$'))
resultado = (((porcentagem * vendas_brutas) / 100) + salario )
if resultado >= 1000:
    print(f'O resultado é {resultado} é iqual ou passa de 1000')
else:
    for c in range(0, 17):
        if resultado >= limites[c] and limites[c+1] >= resultado:
            print(f'O resultado é de {resultado} e está entre {limites[c]} - {limites[c+1]}')
