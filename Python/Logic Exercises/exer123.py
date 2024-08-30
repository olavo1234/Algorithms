from random import randint
from time import sleep

jogos = list()
dados = list()

# print('-='*16)
# print('\tJOGA NA MEGA SENA')
# print('-='*16)

jogadas = int(input('Informe o numero de jogadas: '))
for c in range(0, jogadas):
    while len(dados) < 6: 
        numero_alea = randint(1,60)
        if numero_alea not in dados:
            dados.append(numero_alea)
    jogos.append(dados[:])
    dados.clear()
print()
print(f'-=-=-=\tSORTEANDO {jogadas} JOGOS  -=-=-=')
for c in range(0, jogadas):
        print(f'Jogo {c+1}: {jogos[c]}')
        sleep(1)
print()
print('BOA SORTE!!')
print()
