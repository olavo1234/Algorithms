from time import sleep


def contador(n1, n2, p):
    if n1 > n2:
        print('='*40)
        print(f'Contagem de {n1} até {n2} de {p} em {p}')
        for c in range(n1, n2 - 1, -p):
            print(c,end=' ', flush=True)
            sleep(0.2)
            if c == n2:
                print('FIM!')
    elif p > 0:
        print('='*40)
        print(f'Contagem de {n1} até {n2} de {p} em {p}')
        for c in range(n1, n2+1, p):
            print(c,end=' ', flush=True)
            sleep(0.2)
            if c == n2:
                print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('='*40)
print('Agora é usa vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = abs(int(input('Passo: ')))
if passo == 0:
    contador(inicio, fim, 1)
else:
    contador(inicio, fim, passo)
