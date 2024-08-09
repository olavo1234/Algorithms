matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = soma = 0


for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Adicionar na posição {i+1}X{j+1}: '))
        if matriz[i][j] % 2 == 0:
            spar += matriz[i][j]
    soma += matriz[i][2]
print('-='*20)
for i in range(0,3):
    for j in range(0,3):
        print(f'{matriz[i][j]:^5}',end='')
    print()
print('-='*20)
print(
    f'A soma de todos os valores per são {spar}'
    f'\nA soma dos valores da terceira coluna são {soma}'
    f'\nO maior valor da segunda linha é {max(matriz[1])}'
)
