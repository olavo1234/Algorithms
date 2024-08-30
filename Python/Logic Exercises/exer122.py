# forma usando matematica 

# from math import floor
# nota_50 = 0
# nota_20 = 0
# nota_10 = 0
# nota_1 = 0
# valor = 0
# print("="*43)
# print("\t\tBANCO OLV")
# print("="*43)
# while True:
#     valor += int(input('Qual valor você quer sacar? R$'))
#     if valor <= 0:
#         print('valor invalido')
#         break
#     else:
#         nota_50 = floor(valor / 50)
#         valor = valor % 50
#         nota_20 = floor(valor / 20)
#         valor = valor % 20
#         nota_10 = floor(valor / 10)
#         valor = valor % 20 
#         nota_1 = (valor // 1) % 10
#         break
# if nota_50 > 0:
#     print(f'Total de {nota_50} cédulas de R$50')
# if nota_20 > 0:
#     print(f'Total de {nota_20} cédulas de R$20')
# if nota_10 > 0:
#     print(f'Total de {nota_10} cédulas de R$10')
# if nota_1 > 0:
#     print(f'Total de {nota_1} cédulas de R$1')
# print("="*43)
# print("Volte sempre ao BANCO OLV!, tenha um bom dia!")






# forma usando a lógica

print("="*43)
print("\t\tBANCO OLV")
print("="*43)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1 
    else:
        if totced > 0:
            print(f'total de {totced} cédula de R${ced}')
        if ced == 50:
            ced = 20
        if ced == 20:
            ced = 10
        if ced == 10: 
            ced = 1
        totced = 0
        if total == 0:
            break
print("="*43)
print("Volte sempre ao BANCO OLV!, tenha um bom dia!")
