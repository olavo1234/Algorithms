'''
formulas 
para mulheres: Peso = (62.1 * altura) - 44.7
para homens: Peso = (72.7 * altura) - 58

'''


h = float(input('digite sua altura: '))
peso_mulher = (62.1 * h) - 44.7
print(f'se voce é mulher seu peso ideal é de {peso_mulher:.2f}kg')
Peso_homen = (72.7 * h) - 58
print(f'se voce é um homem seu peso ideal é de {Peso_homen:.2f}kg')

