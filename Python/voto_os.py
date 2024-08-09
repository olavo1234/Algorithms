"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete
feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da
enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0, que encerra a
entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a
percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos,
correspondendo a 40% dos votos.
"""

import asyncio

# calculo e manipulação de dados
async def calcular_dados(usuario_votos, unicos_votos, porcentual_votos, votos_total, sistemas):

    def calcular_votos(lst):
        for c in unicos_votos:
            lst.append(usuario_votos.count(c))


    def calcular_porcent(n_votos, total):
        return ((n_votos / total) * 100)


    calcular_votos(votos_total)
    global tot 
    tot = sum(votos_total)

    for v in votos_total:
        resultado = calcular_porcent(v, tot)
        porcentual_votos.append(resultado)


    for c in range(len(votos_total)):
        # ele vai acrescentar espaços de acordo com a direção definida e o numero de espaço
        print(f'{sistemas[unicos_votos[c]]:<30}{votos_total[c]:<10}{porcentual_votos[c]:.2f}')
        await asyncio.sleep(1)


# demonstração de resultados

def formar_grafico_topo():
    print()
    print(f'{'Sistema Operacional':<30}{'Votos':<10}%')
    print('-'*44)


def formar_grafico_base():
    global tot
    print('-'*44)
    print(f'{'Total':<30}{tot}')
    print()



async def resultado_enquete():
    sistemas = ['None', 'Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
    usuario_votos = list()
    porcentual_votos = list()
    unicos_votos = list()
    votos_total = list()


    print()
    print('''Qual o melhor Sistema Operacional para uso em servidores?

    As possíveis respostas são:

    1- Windows Server
    2- Unix
    3- Linux
    4- Netware
    5- Mac OS
    6- Outro
    ''')

    while True:
        usuario = int(input('Informe o seu voto(0=FIM): '))
        if usuario == 0:
            break
        elif usuario < 0 or usuario > 6:
            print('Codigo invalido, ',end='')
            continue
        usuario_votos.append(usuario)
        if usuario not in unicos_votos:
            unicos_votos.append(usuario)


    # task
    task1 = asyncio.create_task(calcular_dados(usuario_votos, unicos_votos, porcentual_votos, votos_total, sistemas))

    # organizar a ordem
    formar_grafico_topo()
    
    await task1

    formar_grafico_base()

    max_resul = votos_total.index(max(votos_total))
    print(
        f'O Sistema Operacional mais votado foi o {sistemas[unicos_votos[max_resul]]},' 
        f'\ncom {votos_total[max_resul]} votos, correspondendo a {porcentual_votos[max_resul]:.2f}% dos votos'
    )


asyncio.run(resultado_enquete())
