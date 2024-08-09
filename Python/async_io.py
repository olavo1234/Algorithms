# estudar depois o paralelismo

# import time para um melhor aproveitamento usaremos
# await asyncio.sleep() 


import asyncio


async def calcular_imposto(faturamento):
    print(faturamento * 0.1)


async def calcular_bonus_funcionarios(vendas):
    for funcionario in vendas:
        venda = vendas[funcionario]
        print(funcionario, "bonus:", venda * 0.05)
        # time.sleep(1)
        await asyncio.sleep(1)
        # melhora o tempo quasto com o tempo do sleep


async def fechamento():
    vendas = {
        "lira": 1500,
        "joão": 500,
        "amanda": 5000
    }

    faturamento = 1000

    tarefa1 = asyncio.create_task(calcular_bonus_funcionarios(vendas))
    #para realizar o proveitamento de tempo tem que criar uma task - um trabalho específico

    tarefa2 = asyncio.create_task(calcular_imposto(faturamento))

    print('finalizou')

    await tarefa1
    # para fazer o total aproveitamento utilizar o await nas tasks 
    # para ter a otimização de tempo no local da utilização

    await tarefa2

asyncio.run(fechamento())
# para rodar o código assíncrono 
