numeros = []

for _ in range(0, 5):
    valor = int(input('Digite um valor: '))
    if _ == 0:
        numeros.insert(0,valor)
        print(f'Adicionado no final da lista...')
        continue
    for i, numero in enumerate(numeros):
        if valor < numero:
            numeros.insert(i, valor)
            print(f'Adicionado na posição {i}...')
            break
    else:
        for i, numero in enumerate(numeros):
            if numero > valor:
                numeros.insert(i+1, valor)
                print(f'Adicionado na posição {i}...')
                break
            else: 
                continue
        else:
            numeros.insert(len(numeros), valor)
            print(f'Adicionado no final da lista...')
print('*='*20)
print(f'Os valores digitados em ordem foram {numeros}')
