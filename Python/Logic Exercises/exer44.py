"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                     Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

os 5Qs
quantidade em kilos de morangos e maçãs

calcular a tabela de preços com os kilos e calcular um desconto de 10% sequindo a tabela a sequir:
#                     Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.

escrever um algoritimo para ler a quantidade de kilos de morangos e maçãs de 
escrever o valor a ser pago pelo criente 
"""




kg_morango = float(input('digite quantos kilos de morangos comprou: '))
kg_maça = float(input('digite quantos kilos de maçãs comprou: '))
valor = 0 # acrescentar uma variavel com um valor zerado 

if kg_morango <= 5: # se o kg do morango for menor ou iqual a 5 
    valor += kg_morango*2.5 # ele vai somar na variavel valor o calculo de multiplicação
else: # caso não seja menor do que 5
    valor += kg_morango*2.2 # ele soma a multiplicação de outro valor

if kg_maça <= 5: # ele vai fazer o mesmo com a outra condição 
    valor += kg_maça*1.8
else:
    valor += kg_maça*1.5

if (kg_morango+kg_maça) > 5 or valor > 25: # ele vai pegar a soma total das condições 
    valor -= (valor*10)/100 # e substituir o valor com o desconto completo

print(f'o valor a ser pago é de {valor:,.2f}') # ele imprimio resultado na tela

