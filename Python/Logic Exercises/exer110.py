from time import sleep




def maior(*numeros):
    print('-='*20)
    print('valores:',end=' ')
    for i in numeros:
        sleep(0.5)
        print(i,end=' ', flush=True)
    if len(numeros) == 0:
        print('Não foi passado nenhum valor!')
        print(f'E o maior não foi computado')
    else:
        print()
        print(f'Foram digitados {len(numeros)} valores,')
        print(f'e o maior desses valores foi de {max(numeros)}.')



maior()
