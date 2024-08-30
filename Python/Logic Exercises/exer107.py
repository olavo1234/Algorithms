def area(larg, comp):
    resultado = larg * comp
    print(f'A área de um terreno {larg:.0f}X{comp:.0f} é {resultado:.2f}m²')


print('CONTROLE DE TERRENOS')
print('=*'*20)
l = float(input('Informe a largura do terreno(m): '))
c = float(input('Informe o comprimento do terreno(m): '))
area(l, c)
