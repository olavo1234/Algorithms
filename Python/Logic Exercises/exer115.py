# forma com o tratamento de erro
def leiaInt(_=''):
    while True:
        try:
            n = int(input(f'{_}'))
            return n
        except ValueError:
            print('ERRO: digite apenas numeros inteiros!')
            continue


numero = leiaInt('Digite um numero: ')
print(f'O numero digitado foi {numero}')




# forma sem o tratamento
def leiaInt(_=''):
    while True:
        n = str(input(f'{_}'))
        if n.isnumeric():
            int(n)
            return n
        else:
            print('ERRO: informe apenas numeros inteiros')
            continue


numero = leiaInt('Digite um numero: ')
print(f'O numero digitado foi {numero}')
