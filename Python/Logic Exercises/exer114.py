# usando o tratamento de erros e exeções
def ficha(jogador, gols=0):
    if nome_jogador == '':
        jogador = '<indefined>'
    print(f'O jogador: {jogador}, fez {gols} gols.')



nome_jogador = str(input('nome: ')).strip()
try: 
    numero_gols = int(input('gols: '))
    ficha(nome_jogador,numero_gols)
except ValueError:
    ficha(nome_jogador)







# usando o isnumeric
def ficha(joga='undefined', gol=0):
    print(f'O jogador {joga} fez {gol} gol(s) no campeonato.')



n = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    int(g)
else:
    g=0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
