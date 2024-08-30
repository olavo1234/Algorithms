def notas(*nota, sit=False):
    """
    A função notas calcula estatísticas de notas de alunos.

    Parâmetros:
    - *nota (float): Uma sequência de notas dos alunos.
    - sit (bool): Se True, adiciona a situação do aluno (opcional).

    Retorna:
    Um dicionário contendo:
    - 'total': Total de notas.
    - 'maior': Maior nota.
    - 'menor': Menor nota.
    - 'média': Média das notas.

    Se sit=True, adiciona:
    - 'situação': Situação do aluno (razoável, ruim, ótimo).

    Exemplo de uso:
    resp = notas(8, 9, 10, 10, sit=True)
    print(resp)
    """
    cont = somaNota = maiorNota = menorNota = 0
    for valor in nota:
        cont += 1
        somaNota += valor
        if cont == 1:
            maiorNota = valor
            menorNota = valor
        else:
            if valor > maiorNota:
                maiorNota = valor
            if valor < menorNota:
                menorNota = valor
    media = somaNota / cont
    dados = {'total': cont, 'maior': maiorNota, 'menor': menorNota, 'média':media}
    if sit:
        if media >= 5 and media <= 6:
            dados['situação'] = 'razoável'
        elif media < 5:
            dados['situação'] = 'ruim'
        elif media > 6:
            dados['situação'] = 'ótimo'
    return dados


resp = notas(8,9,10,10,sit=True)
print(resp)
