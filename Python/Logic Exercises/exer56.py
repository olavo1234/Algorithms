"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

soma = 0
comeco = int(input("digite um numero inteiro para iniciar: "))
fim = int(input("digite um numero inteiro para finalizar: ")) 
for n in range(comeco +1, fim):
    soma += n
    print(n)
print(f'soma = {soma}')
