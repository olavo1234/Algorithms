def leiaInt(_=''):
    try:
        while True:
            try:
                n = int(input(f'{_}'))
                return n 
            except (ValueError, TypeError):
                print(f'ERRO: digite um némero inteiro válido')
    except KeyboardInterrupt:
        print('\nERRO: usuário preferiu não informar o número')
        return ''


def leiaFloat(_=''):
    try:
        while True:
            try:
                n = float(input(f'{_}'))
                return n 
            except (ValueError, TypeError):
                print(f'ERRO: digite um numero float válido')
    except KeyboardInterrupt:
        print('\nERRO: usuário preferiu não informar o número')
        return ''


numero = leiaInt('digite um numero inteiro: ')
print(numero)

numero = leiaFloat('digite um numero float: ')
print(numero)
