"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e
valor da parcela.

# Os juros e a quantidade de parcelas seguem a tabela abaixo:
#     Quantidade de Parcelas    % de Juros sobre o valor inicial da dívida
#     1                          0
#     3                         10
#     6                         15
#     9                         20
#     12                        25

# Exemplo de saída do programa:
#     Valor da Dívida  Valor dos Juros  Quantidade de Parcelas  Valor da Parcela
#     R$ 1.000,00      R$0                1                       R$  1.000,00
#     R$ 1.100,00      R$100              3                       R$    366,00
#     R$ 1.150,00      R$150              6                       R$    191,67
"""


# interssante
# ele criou uma equação que vai ficar calculando o juros de acordo com as parcelas 
# gabarito
valor_da_divida = float(input("Digite o valor da dívida: "))
parcelas = 1
juros = 0
print(
    "|Valor da Dívida|Valor dos Juros|Quantidade das Parcelas|Valor da Parcela|"
)
while True:
    # ? A fórmula abaixo foi encontrada usando a equação da reta
    # ? y - y0 = m * (x - x0), com y = 15, y0 = 10, x = 6 e x0 = 3
    # ? y -> Percentual de juros | x -> Quantidade de parcelas
    juros = (5 / 3) * parcelas + 5
    # ? Não é uma reta perfeita pois quando x=1, y=0
    if parcelas == 1:
        juros = 0

    valor_do_juros = valor_da_divida * (juros / 100)
    valor_total = valor_da_divida + valor_do_juros
    valor_da_parcela = valor_total / parcelas
    print(
        f"|R$ {valor_total:.2f}\t"
        f"|R$ {valor_do_juros:.2f}\t"
        f"|{parcelas}\t\t\t"
        f"|R$ {valor_da_parcela:.2f}"
    )
    if parcelas == 1:
        parcelas -= 1
    parcelas += 3
    if parcelas > 12:
        break










# jeito sem o laço de repetição 
# forma mais trabalhoso e longo

# qantidade_parc = 0
# divida = float(input('Informe o valor da divida: '))
# while True:
#     juros_0 = (divida * 0) / 100
#     if juros_0 == juros_0:
#         quantidade_parc_0 = 1
#         total_0 = divida + juros_0
#     juros_10 = (divida * 10) / 100
#     if juros_10 == juros_10:
#         quantidade_parc_10 = 3
#         total_10 = divida + juros_10
#     juros_15 = (divida * 15) / 100
#     if juros_15 == juros_15:
#         quantidade_parc_15 = 6
#         total_15 = divida + juros_15
#     juros_20 = (divida * 20) / 100
#     if juros_20 == juros_20:
#         quantidade_parc_20 = 9
#         total_20 = divida + juros_20
#     juros_25 = (divida * 25) / 100
#     if juros_25 == juros_25:
#         quantidade_parc_25 = 12
#         total_25 = divida + juros_25
#     break
# print(f"""     
# Valor da Dívida  Valor dos Juros  Quantidade de Parcelas  Valor da Parcela
# R$ {total_0:,.2f}      R$ {juros_0:,.2f}                {quantidade_parc_0}                       R$ {total_0/quantidade_parc_0:,.2f}
# R$ {total_10:,.2f}      R$ {juros_10:,.2f}              {quantidade_parc_10}                       R$ {total_10/quantidade_parc_10:,.2f}
# R$ {total_15:,.2f}      R$ {juros_15:,.2f}              {quantidade_parc_15}                       R$ {total_15/quantidade_parc_15:,.2f}
# R$ {total_20:,.2f}      R$ {juros_20:,.2f}              {quantidade_parc_20}                       R$ {total_20/quantidade_parc_20:,.2f}
# R$ {total_25:,.2f}      R$ {juros_25:,.2f}              {quantidade_parc_25}                      R$ {total_25/quantidade_parc_25:,.2f}
# """)





