"""
Faça um Programa que peça dois números e imprima o maior deles.

passos
pedir dois numero ao usuario
declaro uma variavel e coloco os numeros 
comparar eles com um sinal de maior 
fazer uma estrutura de if para exibir o maior  
else para exibir corretamente o maior  
exibir corretamente na tela o numero maior

os 5Qs 
2 numeros do usuario
comparar e imprimir o maior desses numeros na tela 
exibir corretamente na tela o numero maior
exibir na tela o numero maior 
5 
input"informe um numero: "
input"informe outro numero: "
if numero_1 > mumero_2
print"numero_1"
 else
  print"numero_2" 

"""


num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))
if num1 > num2:
    print(f'entre os numeros {num1} e {num2}, o numero maior é {num1}')
else:
    print(f'entre os numeros {num1} e {num2}, o numero maior é {num2}')