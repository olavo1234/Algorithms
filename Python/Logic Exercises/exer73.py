"""
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99,
com cerca de 10 caixas.

Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma
tabela que contém o número de itens que o cliente comprou e ao lado
o valor da conta.

Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente
está levando e olhar na tabela de preços.

Você foi contratado para desenvolver o programa que monta esta
tabela de preços, que conterá os preços de 1 até 50 produtos,
conforme o exemplo abaixo:

    Lojas Quase Dois - Tabela de preços
    1 - R$ 1.99
    2 - R$ 3.98
    ...
    50 - R$ 99.50
"""

# todos os itens custa 1.99
# fazer uma tabela que vai mostrar a quantidade dos itens e a tebela com a soma dos preços
print('=*'*30)
print('Lojas Quase Dois - Tabela de preços')
print('=*'*30)
for c in range(1,51):
    print(f'{c:2} - R${c*1.99:.2f}')
print('=*'*30)
