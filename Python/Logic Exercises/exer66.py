"""
Altere o programa de cálculo dos números primos, informando , caso o número não
seja primo, por quais número ele é divisível.
"""


numero = int(input("Digite um numero inteiro: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        print(f'{numero} não é primo!')
        break
for i in range(2, numero):# segundo laço for para exibir os numeros divisiveis
    if numero % i == 0:
        print(f'divisivel por {i}')
if primo:
    print(f'{numero} é primo!')



# gabarito
# numero = int(input("Digite um numero inteiro: "))
# primo = True
# for i in range(2, numero):
#     if numero % i == 0:
#         primo = False
#         print(f"{numero} não é primo! É divisível por {i}.")
# if primo:
#     print(f"{numero} é primo!")
