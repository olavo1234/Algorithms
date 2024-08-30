"""
os 5Qs

o tipo de carne e a quantidade de carne comprada e o tipo de pagamento

o cliente deve comprar apenas uma carne com a quantidade que desejar se o 
cliente comprar com o cartao ele receberar um desconto de 5% sobre o (TOTAL) da compra
sequindo a tabela de preços:
#                     Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

se for comprada com o cartao tabajara terá 5% de desconto
para escrever o cupon fiscal todas as varievel que ter um so valor

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra:
#    tipo de carne
#    quantidade de carne
#    preço total
#    tipo de pagamento
#    valor do desconto
#    valor a pagar.

"""







# jeito errado


"""
carne = str(input("digite a opção de carne desejada: file duplo, alcatra, picanha: ")).strip().upper()
quantidade = float(input('digite a quantidade em kg de carne desejada: '))
cartao = str(input('tipo de pagamento: ')).strip().upper()
valor = 0
desconto = 0

if carne == "FILE DUPLO":
    if quantidade <= 5:
        valor = quantidade*4.90
    else:
        valor = quantidade*5.80

if carne == "ALCATRA":
    if quantidade <= 5:
        valor = quantidade*5.90
    else:
        valor = quantidade*6.80

if carne == "PICANHA":
    if quantidade <= 5:B
        valor = quantidade*6.90
    else:
        valor = quantidade*7.80

if cartao == "cartao tabajara" or cartao == "cartao":
    valor -= (valor*5) /100
    desconto = (valor*5) /100




print(f"{valor} e {desconto}")

"""








# PRINT DO CUPON FISCAL na estrutura do codigo 


carne = input("Digite F para filé duplo, A para alcatra e P para picanha: ")
peso = float(input("Digite quantos quilos dessa carne vai comprar: "))
pagamento = input("Dinheiro ou cartão tabajara (5% de desconto)? D ou C: ")
preco_total = 0

print("\nHipermercado Tabajara\nCupom fiscal\n")
if carne == "F" or carne == "f":
    print("Item: Filé Duplo")
    if peso > 5:
        preco_total = peso * 5.8
    else:
        preco_total = peso * 4.9
elif carne == "A" or carne == "a":
    print("Item: Alcatra")
    if peso > 5:
        preco_total = peso * 6.8
    else:
        preco_total = peso * 5.9
elif carne == "P" or carne == "p":
    print("Item: Picanha")
    if peso > 5:
        preco_total = peso * 7.8
    else:
        preco_total = peso * 6.9
print(f"Quantidade: {peso:.2f}Kg")
print(f"Preço total: R${preco_total:.2f}")
if pagamento == "D" or pagamento == "d":
    print("Tipo de pagamento: Dinheiro")
    desconto = 0
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${(preco_total - desconto):.2f}")
elif pagamento == "C" or pagamento == "c":
    print("Tipo de pagamento: Cartão Tabajara")
    desconto = preco_total * 5 / 100
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${(preco_total - desconto):.2f}")


