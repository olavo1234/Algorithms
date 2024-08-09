# sistema modularizado

# o porametro opcional lst é uma lista
def cadastro(lst=[]):
    tabela_opcao = lst
    print('='*30)
    print('\tMENU PRINCIPAL')
    print('='*30)
    for v, i in enumerate(tabela_opcao):
        print(f'{v+1} - {i}')
    print()


def cabecario(msg=''):
    tamanho = (len(msg) + 4)
    print('='*tamanho)
    print(f'  {msg}')
    print('='*tamanho)
