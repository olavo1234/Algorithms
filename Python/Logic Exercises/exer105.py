"""
Faça um programa que leia um número indeterminado de valores, correspondentes a
notas, encerrando a entrada de dados quando for informado um valor igual a -1
(que não deve ser armazenado).

Após esta entrada de dados, faça:
    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados,
        um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados,
        um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;
"""



notas = list()
acima_da_media = 0
quantidade_abaixo = 0


while True:
    nota = int(input('Digite um numero(-1 para): '))
    if nota == -1:
        break
    else:
        notas.append(nota)
quantidade = len(notas)
soma = sum(notas)
media = soma / quantidade 
print(f'A quantidade de valores foi de {quantidade}')
print('\nOs numeros são:')
for n in notas:
    print(n, end='; ')
print()
notas.reverse()
for notas_reversas in notas:
    print(notas_reversas)
print(f'\nA soma dos valores é de {soma}')
for c in notas:
    if c > media:
        acima_da_media += 1 
    if c < 7:
        quantidade_abaixo += 1
print(f'\nA média dos valores é de {media}')
print(f'\nQuantidade de valores acima da média é de {acima_da_media}')
print(f'\nQuantidade de valores abaixo de sete é de {quantidade_abaixo}')
print('\n>>> PROGRAMA ENCERRADO <<<')
