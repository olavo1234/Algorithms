"""
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em
reconhecimento ao bom resultado alcançado durante o ano que passou.
Para isto contratou você para desenvolver a aplicação que servirá como uma
projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os
representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

    # Cada funcionário receberá o equivalente a 20% do seu salário bruto de
    # dezembro;
    # O piso do abono será de 100 reais, isto é, aqueles funcionários cujo
    # salário for muito baixo recebem este valor mínimo;
    # Neste momento, não se deve ter nenhuma preocupação com colaboradores com
    # tempo menor de casa, descontos, impostos ou outras particularidades.

Seu programa deverá permitir a digitação do salário de um número indefinido
(desconhecido) de salários.
Um valor de salário igual a 0 (zero) encerra a digitação.
Após a entrada de todos os dados o programa deverá calcular o valor do abono
concedido a cada colaborador, de acordo com a regra definida acima.
Ao final, o programa deverá apresentar:
    # O salário de cada funcionário, juntamente com o valor do abono;
    # O número total de funcionários processados;
    # O valor total a ser gasto com o pagamento do abono;
    # O número de funcionários que receberão o valor mínimo de 100 reais;
    # O maior valor pago como abono;

Exemplo:
Projeção de Gastos com Abono
============================

Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0

Salário    - Abono
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00

Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo foi pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
"""


# 100/ 300/ 500/ # salários menores que 500 entra no piso
# abono 20/ 60/ 100
# piso de 100 = a todos que não chegaram no valor do mesmo

salar_brutos = list()
abonos = list()
porcentagem = 20
piso_salarial = 100
cont_piso = 0

print('Projeção de Gastos com Abono')
print('='*28)
print()
while True:
    salario = float(input('Informe o seu salário: R$'))
    if salario == 0:
        break
    elif salario < 0:
        print('Inválido, ',end='')
        continue
    salar_brutos.append(salario)
# \\


def calcular_abono(salario):
    return ((salario * porcentagem) / 100)


for v in salar_brutos:
    if v <= 500:
        cont_piso += 1
        abonos.append(piso_salarial)
    else:
        resultado = calcular_abono(v)
        abonos.append(resultado)

# \\

# demonstração de resultado
print()
print(f'{'Salário':<10}{'-':^4}{'Abono'}')
for c in range(len(salar_brutos)):
    print(f'R$ {salar_brutos[c]:<7.2f}{'-':^4}R$ {abonos[c]:.2f}')
print()
print(
    f'Foram processados {len(salar_brutos)} colaboradores'
    f'\nTotal gasto com abonos: R${sum(abonos):.2f}'
    f'\nValor mínimo foi pago a {cont_piso} colaboradores'
    f'\nMaior valor de abono pago: R${max(abonos):.2f}'
)
