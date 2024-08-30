"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais
alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um
programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso.

O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero)
no campo código.

Ao encerrar o programa também deve ser informados os códigos e valores do
clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média
das alturas e dos pesos dos clientes.
"""



cont = tot_peso = tot_altu = alto = baixo = gordo = magro = cod_alto = cod_baixo = cod_gordo = cod_magro = 0
while True:
    cont += 1
    print(F'ª{cont} PESSOA')
    codigo = int(input('Informe o seu codigo: '))
    if codigo == 0:
        break
    altura = float(input('Digite o sua altura: '))
    tot_altu += altura
    peso = float(input('Digite o seu peso: '))
    tot_peso += peso
    if cont == 1:
        gordo = magro = peso
        alto = baixo = altura
        cod_alto = cod_baixo = cod_gordo = cod_magro = codigo 
    else:
        if peso > gordo:
            gordo = peso
            cod_gordo = codigo
        if peso < magro:
            magro = peso
            cod_magro = codigo
        if altura > alto:
            alto = altura
            cod_alto = codigo
        if altura < baixo:
            baixo = altura
            cod_baixo = codigo
    media_altu = tot_altu / cont
    media_peso = tot_peso / cont
print(
    f'Cliente mais alto {alto:.2f} com o codigo {cod_alto}'
    f'\nCliente mais baixo {baixo:.2f} com o codigo {cod_baixo}'
    f'\nCliente mais gordo {gordo:.2f} com o codigo {cod_gordo}'
    f'\nCliente mais magro {magro:.2f} com o codigo {cod_magro}'
    f'\nA média da altura é de {media_altu:.1f} e do peso {media_peso:.1f}'
)
