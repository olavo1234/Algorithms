"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.
"""

cont = soma =temp_baixa = temp_alta = 0 # forma resumida se todos for 0
while True:
    temperatura = float(input('Informe a temperatura: '))
    cont += 1
    soma += temperatura
    if cont == 1:
        temp_baixa = temp_alta = temperatura
    else:
        if temperatura > temp_alta:
            temp_alta = temperatura
        if temperatura < temp_baixa:
            temp_baixa = temperatura
    alt = str(input('Deseja continuar? (S/N): ')).strip()[0]
    if alt in 'Nn':
        break
media = soma / cont
print(
    f'\nA maior temperatura é de {temp_alta}'
    f'\nA menor temperatura é de {temp_baixa}'
    f'\nA média é de {media:.1f}'
)
