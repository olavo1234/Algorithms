"""
Altere o programa de cálculo do fatorial (61), permitindo ao usuário calcular o
fatorial várias vezes e limitando o fatorial a números inteiros positivos e
menores que 16.
"""

# continuar = True
# while continuar: 
#     numero = int(input("Digite um numero: "))
#     while numero < 0 or numero > 16:
#         print('invalido, tente novamente!')
#         numero = int(input('Digite um numero: '))
#     else:
#         fatorial = numero
#         for c in range(numero-1, 0, -1): 
#             fatorial *= c
#         print(f'{numero}!:',end="")
#         ultimo = "1"
#         for c in range(numero, 1, -1):
#             print(c,end=".")
#         print(ultimo, end="")
#         print(f' = {fatorial:,.0f}')
#         continuar = (
#             True if input('Digite C-continuar e P-parrar: ').upper() == "C" else False 
#         )  


while True:
    numero = int(input("Digite um numero: "))
    if not 0 < numero < 16:
        continue# quando for a condição acima o loop voltara ao topo 
    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")
    if input("Deseja continuar? (S/N): ").upper() != "S":
        break
