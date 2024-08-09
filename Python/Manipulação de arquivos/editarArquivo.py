DIRETORIO = ("c:/exercícios/python/exe115/cadastro.txt")

def confirmaArquivo():
    try:
        with open(DIRETORIO, "r") as file:
            pessoas = file.readlines()
    except FileNotFoundError:
        print('ATENÇÃO: Você não possui um arquivo.txt; Criando um...')
        with open(DIRETORIO, "w") as file:
            pass


def lerArquivo():
    with open(DIRETORIO, "r", encoding="utf-8") as file:
        pessoas = file.read()
        for pessoa in pessoas:
            print(pessoa,end='')
    print()


def adicionarDados(nome, idade):
    with open(DIRETORIO, "a") as editar:
        editar.write(f'\n{nome:<30}{idade:} anos')
