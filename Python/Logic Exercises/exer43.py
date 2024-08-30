"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

os 5Qs

o numero de litros de vendidos e o tipo de conbustivel (codificado da seguinte forma: A-álcool, G-gasolina)

calcular os conbustiveis com a sequinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro

sequindo os sequintes preços gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""




'''
litros = float(input('digite quantos litros quer abastecer: '))
tipo_conbustivel = str(input('digite A para álcool e G para gasolina: ')).upper()
preco_litro_g = 2.50 * litros
preoco_litro_a = 1.90 * litros

if tipo_conbustivel == "G":
    if litros > 20:
        print(f'voce pagara R${preco_litro_g - ((preco_litro_g*6)/100):,.2f} com 6% de decontos')
    elif litros <= 20:
        print(f'voce pagara R${preco_litro_g - ((preco_litro_g*4)/100):,.2f} com 4% de desconto')
elif tipo_conbustivel == "A":
    if litros > 20:
        print(f'voce pagara R${preoco_litro_a - ((preoco_litro_a*5)/100):,.2f} com 5% de descontos')
    elif litros <= 20:
        print(f'voce pagara R${preoco_litro_a - ((preoco_litro_a*3)/100):,.2f} com 3% de descontos')
'''






# jeito menos parrudo
# com o mesmo resultado do de cima

litros = float(input("Digite quantos litros você quer abastecer: "))
combustivel = input("Digite A para álcool ou G para gasolina: ")
preco = 0 # variavel para inprimir que ira mudar o valor conforme a variavel
if combustivel == "A" or combustivel == "a":
    preco = litros * 1.9
    if litros <= 20:
        preco -= 1.9 * litros * 3 / 100 # ele ira tirar o valor anterior e colocar o valor do desconto ja subtraido
    else:
        preco -= 1.9 * litros * 5 / 100
elif combustivel == "G" or combustivel == "g":
    preco = litros * 2.5
    if litros <= 20:
        preco -= 2.5 * litros * 4 / 100
    else:
        preco -= 2.5 * litros * 6 / 100
print(f"O preço a pagar é R${preco:.2f}")

