def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: não vota'
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: o voto opcional'
    else:
        return f'Com {idade} anos: o voto é obrigatório'


resultado = voto(2007)
print(resultado)
