"""
Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.
"""

soma = 0
n = int(input("Digite n: "))
m = 1
print("S = ", end="")
for i in range(1, n + 1):# n+1 para iqualar a 1 não a 0
    print(f"{i}/{m}", end="")
    # esse idf irá determinar qundo é para colocar + ou .
    # ele irá comparar se o contador i for menor que o n 
    # ele irá colocar o + e irá prossequir
    # caso ele seja maior quer dizer que aporação acabou .
    if i < n and n > 1:
        # n > 1 para não entrar numeros negativos
        print(" + ", end="")
    else:
        print(".")
    soma += i / m
    # ele irá senpre somar com 2 para continuar a sequencia
    m += 2
print(f"A soma da série deu {soma:.2f}")
