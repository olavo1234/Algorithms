"""
O cardápio de uma lanchonete é o seguinte:
    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades
desejadas.

Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total
geral do pedido.

Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""


tot = quan_100 = quan_101 = quan_102 = quan_103 = quan_104 = quan_105 = 0
print('-=' * 40)
print('CARDAPIO')
print("""
Especificação   Código  Preço
--------------------------------
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
""")
print('-=' * 20)
while True:
    cod_item = int(input('Digite o codigo do item: '))
    if cod_item < 100 or cod_item > 105:
        print('Codigo invalido')
        continue
    quant = int(input('Digite a quantidade desejada: '))
    if cod_item == 100:
        tot += 1.20 * quant
        quan_100 += quant
    elif cod_item == 101:
        tot += 1.30 * quant
        quan_101 += quant
    elif cod_item == 102:
        tot += 1.50 * quant
        quan_102 += quant
    elif cod_item == 103:
        tot += 1.20 * quant
        quan_103 += quant
    elif cod_item == 104:
        tot += 1.30 * quant
        quan_104 += quant
    elif cod_item == 105:
        tot += 1.00 * quant
        quan_105 += quant
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
# usar a tabelação
print(
    '\nFechamento do pedido'
    '\nCodigo  |  Quantidade  |  Preço unitario  |  Preço total'
)
if quan_100 > 0:
    print(f'100 \t\t{quan_100}\t     R$1.20\t\tR${quan_100*1.20:,.2f}')
if quan_101 > 0:
    print(f'101 \t\t{quan_101}\t     R$1.30\t\tR${quan_101*1.30:,.2f}')
if quan_102 > 0:
    print(f'102 \t\t{quan_102}\t     R$1.50\t\tR${quan_102*1.50:,.2f}')
if quan_103 > 0:
    print(f'103 \t\t{quan_103}\t     R$1.20\t\tR${quan_103*1.20:,.2f}')
if quan_104 > 0:
    print(f'104 \t\t{quan_104}\t     R$1.30\t\tR${quan_104*1.30:,.2f}')
if quan_105 > 0:
    print(f'105 \t\t{quan_105}\t     R$1.00\t\tR${quan_105*1.00:,.2f}')
print(f'Total do pedido: R${tot:,.2f}')
print('-=' * 40)
