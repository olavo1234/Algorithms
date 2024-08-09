matriz = [[0,0,0],[0,0,0],[0,0,0]]
cont = 0

while True:
    cont +=1 
    for i in range(0,3):
        for j in range(0,3):
            if cont == 1:
                matriz[i][j] = int(input(f'Adicionar na posição {i+1}X{j+1}: '))
            else:
                matriz[i][j] *= valor
    print('A matriz é:')
    for i in range(0,3):
        for j in range(0,3):
            print(f'{matriz[i][j]:^5}',end='')
        print()
    if cont == 1:
        valor = int(input('Digite o valor para multiplicar: '))
        continue
    else:
        break
