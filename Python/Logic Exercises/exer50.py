"""
Altere o programa anterior permitindo ao usuário informar as populações e as
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""


# meu jeito com validação de entrada
continuar = True
while continuar:
    populacao_A = float(input('informe a população do pais A: '))
    while populacao_A < 0:# utilizar o while em uma condição para sempre repetilo 
        print('invalido, tente novamente')
        populacao_A = float(input('informe a população do pais A: '))# repetir o input para o codigo pressequir

    populacao_B = float(input('informe a população do pais B: '))
    while populacao_B < 0:
        print('invalido, tente novamente')
        populacao_B = float(input('informe a população do pais B: '))

    taxa_anual_A = float(input("digite a taxa anual do pais A: "))
    taxa_anual_B = float(input("digite a taxa anual do pais B: "))
    anos = 0
    print("-"*30)
    while True:# começo do while da operação
        anos +=1 
        populacao_A *= 1 + (taxa_anual_A / 100)
        populacao_B *= 1 + (taxa_anual_B / 100)
        if populacao_A >= populacao_B:
            print(
                f'Demorou {anos:.0f} anos para a populção de A passar a de B.'
                f'\nA tem {populacao_A:,.0f} habitantes e '
                f'B tem {populacao_B:,.0f} habitantes '
            )
            break# fim
    print("-"*30)
    continuar = (# variavel continuar com um valore booleano utilizando o if ternario 
        True if input("deseja continuar (S/N)? => ").upper() == "S" else False
    )# se for s ira ser True o codigo irá sequir/ se for n irá ser False o codigo irá parar 
    print("-"*30)






# gabarito sem validação de entrada
"""
continuar = True# DEFINIU uma variavel de valor booleano em contiuar
while continuar:# colocou a variavel de valor True no laço while
    populacao_a = float(input("Digite a população de A: "))# input feito do modo normal
    populacao_b = float(input("Digite a população de B: "))
    crescimento_a = float(
        input("Digite o crescimento percentual da população de A: ")
    )
    crescimento_b = float(
        input("Digite o crescimento percentual da população de B: ")
    )
    anos = 0 # fim do laço
    while True:# outro while que vai repetir o que ta dentro e irá para com o breah
        anos += 1
        populacao_a *= 1 + (crescimento_a / 100)
        populacao_b *= 1 + (crescimento_b / 100)
        if populacao_a >= populacao_b:
            print(
                f"Demorou {anos} anos para a população de "
                "A passar ou igualar a de B."
                f"\nA tem {populacao_a:.0f} habitantes e "
                f"B tem {populacao_b:.0f}."
            )
            break# fim do while da operação
    continuar = (# irá retorna a variavel continuar se o usuario responder S ira ser true 
        True if input("Deseja continuar (S/N)? > ").upper() == "S" else False
    )# SE RESPONDER N IRA SER FALSE o programa irá se finalizado
"""