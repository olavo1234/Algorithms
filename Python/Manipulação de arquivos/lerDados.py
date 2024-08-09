from tabela import cadastro, cabecario
from editarArquivo import adicionarDados, confirmaArquivo, lerArquivo
from time import sleep

confirmaArquivo()

while True:
    cadastro(['Ver pessoas cadastradas', 'Adicionar pessoas', 'Sair do programa'])
# \\
    try:
        opcao = int(input('informe a sua opção: '))
        if opcao > 3 or opcao < 1:
            print('ERRO: Opção inválida.')
            continue
    except (ValueError, TypeError, SyntaxError):
        print('ERRO: Dado incorreto.')
        continue
    sleep(1)
    print()
# \\ tratamento de exceção
# \\
    if opcao == 1:
        cabecario('VISUALIZAR DADOS')
        lerArquivo()
        print()
    sleep(1)
# ler aquivo de texto
# \\
    if opcao == 2:
        cabecario('NOVO CADASTRO')
        novo_cadastro_nome = str(input('Nome: '))
        novo_cadastro_idade = str(input('Idade: '))
        adicionarDados(novo_cadastro_nome, novo_cadastro_idade)
        print()
    sleep(1)
# adicionar dados no arquivo
# \\
    if opcao == 3:
        cabecario('FINALIZANDO...')
        break
