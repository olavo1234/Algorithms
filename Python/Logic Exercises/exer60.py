"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

n = int(input("Que termo deseja encontrar: "))# numero que vai repetir
ultimo = 1# quarda o ultimo numero da sequencia 
penultimo = 0# quarda o penultimo numero da sequencia  
for _ in range(n):# começa apartir do 1 e vai até n
    print(penultimo)# primeiro numero 0
    termo = ultimo # variavel termo vai ficar recebendo o ultimo termo 
    ultimo += penultimo# a sequencia vai andar com o valor do ultimo vai ficar somando no penultimo 
    penultimo = termo# o ultimo vai receber o termo da conta de mais 
# ele fez um loop onde as variaveis vão se substituir e trocar de valores
# fazendo a soma
