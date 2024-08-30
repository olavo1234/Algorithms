from random import randint
cont = 0
while True:
    print("~-"*30)
    print("\t\tVAMOS JOGAR IMPAR OU PAR")
    print("~-"*30)
    n_usuario = int(input('Digite um valor: '))
    computador = randint(1,n_usuario)
    soma = n_usuario + computador
    escolha = ' '
    while escolha not in "PpIi":# irá se repetir até o valor ser p ou i
        escolha = str(input("par ou impar? P/I: ")).strip()[0]
    print("~-"*30)
    if soma % 2 == 0:
        print(f'Você jogou {n_usuario} e o computador {computador}. total de {soma} deu par')
        if escolha in "Pp":
            print(
                'Sua escolha foi PAR'
                '\nVOCÊ VENCEU!'
                '\nVamos outra vez...'
            )
            cont += 1
        else:
            print(
                'Sua escolha foi IMPAR'
                '\nVOCÊ PERDEU!'
            )
            break
    if soma % 2 != 0:
        print(
        f'voce jogou {n_usuario} e o computador {computador}. total de {soma} deu IMPAR')
        if escolha in "Ii":
            print(
                'Sua escolha foi IMPAR'
                '\nVOCÊ VENCEU!'
                '\nVamos outra vez...'
            )
            cont += 1
        else:
            print(
                'Sua escolha foi PAR'
                '\nVOCÊ PERDEU!'
            )
            break
print("~-"*30)
print(f"GAME OVER! você venceu {cont} vez(es)")
