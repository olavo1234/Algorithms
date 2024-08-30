"""
Faça um programa que leia e valide as seguintes informações:
#    Nome: maior que 3 caracteres;
#    Idade: entre 0 e 150;
#    Salário: maior que zero;
#    Sexo: 'f' ou 'm';
#    Estado Civil: 's', 'c', 'v', 'd';


os 5Qs

um nome, idade, salario, sexo, estado civil

analisar cada um de acordo com os criterios e validar

nome: maior que 3 caracteres;
idade: entre o e 150;
salario: maior que 0;
sexo: 'f' ou 'm';
estado civi: 's', 'c', 'v', 'd'

ler e validar as informções a cima

"""

nome = str(input('Digite o seu nome: '))
while len(nome) < 4:# o laço while para qunado ver um input e so continua quando a condição dele for correrta
    print('nome invalido, tente novamente')
    nome = str(input('Digite o seu nome: '))

idade = int(input('digite a sua idade: '))
while idade < 0 or idade > 150:
    print('idade invalida, tente novamente')
    idade = int(input('digite a sua idade: '))

salario = float(input('digite o seu salario: '))
while salario < 0:
    print('salario invalido, tente novamente')
    salario = float(input('digite o seu salario: '))

sexo = input('digite m-masculino ou f-feminino: ').upper()
while sexo != "M" and sexo != "F":
    print('genero invalido, tente novamente')
    sexo = input('digite m-masculino ou f-feminino: ').upper()

estado_civil = input('''digite um dos estado civil 
[ s ] solteiro
[ c ] casado
[ v ] viúvo(a)
[ d ] divorciado
seu estado civil é: ''').upper()

while (
    estado_civil != "S" 
    and estado_civil != "C" 
    and estado_civil != "V" 
    and estado_civil != "D"
):
    print('estado civil invalido, tente novamente')
    estado_civil = input('''digite um dos estado civil 
[ s ] solteiro
[ c ] casado
[ v ] viúvo(a)
[ d ] divorciado
seu estado civil é: ''').upper()


