def fatorial(numero, show=False):
    cont = 1
    resultado = 1
    while numero >= 2:
        resultado *= numero
        if show:
            if cont == 1:
                print(f'{numero}!:', end=' ')
            print(numero,end=' x ')
            if numero == 2:
                print('1 = ',end='')
        numero -= 1
        cont += 1 
    else:
        return resultado




print(fatorial(5, show=True))
