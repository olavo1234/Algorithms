from random import randint

numeros = list()


def sortear(lst):
    for _ in range(5):
        lst.append(randint(1,10))
    print('Os valores sorteados foram', end=' ')
    print(*lst, sep=', ')


def somarPar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos pares é de {soma}')



sortear(numeros)
somarPar(numeros)
