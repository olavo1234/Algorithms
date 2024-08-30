"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
   A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete; 
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
    
passos 
ler e entender o problema 
pedir a primeira nota
pedir a segunda nota 
gravar cada um em uma variavel 
soamar as variaveis das notas e dividir por 2
gravar em uma variavel chamado nota
fazer um laço if com os sinais de comparaçao 
"media" >= 7  exibir "aprovado"
"media" < 7 exibir "reprovado"
media = 10 exibir "aprovado com distinçao"

os 5Qs 
preciso de 2 notas do usuario
O programa deve calcular a média alcançada por aluno e apresentar
apresentar as mensagens corretamente de acordo com o resultado
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete; 
A mensagem "Aprovado com Distinção", se a média for igual a dez.
5

valor1 = input"digite o primeiro valor: "
valor2 = input"digite o segundo valor: "
media = valor1 + valor2 /2
if media >= 7
print"aprovado"
elif media < 7 
print"reprovado"
elif media = 10 
print"aprovado com distinçao"
"""

valor1 = float(input('digite o primeiro valor: '))
valor2 = float(input('digite o segundo valor: '))
media = (valor1 + valor2) /2
if media == 10:
    print('aprovado com distinção')
elif media >= 7:
    print('aprovado')
else: 
    print('reprovado')
