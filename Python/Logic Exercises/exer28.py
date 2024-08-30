"""
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.

passos
ler e entender o que se esta sendo pedido
perguntar ao usuario em que turno se estuda
pedir parar digitar M-matutino ou V-Vespertino ou N- Noturno.
com isso imprimir na tela as sequintes mensagens "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.

os 5Qs
pedir a o usuario para digitar M-matutino ou V-Vespertino ou N- Noturno.
ler e imprimir as sequintes mensagens Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!"
caso o usuario digite outra coisa exibir "Valor Inválido!"
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.
5 
turno = input"digite em que turno está M-matutino ou V-Vespertino ou N- Noturno: " 
if turno == "m" or turno == "M"
print"bom dia!"
elif turno == "v" or turno == "V" 
print"boa tarde!"
elif turno == "n" or turno == "N"
print"boa noite!"
else:
print"valor invalido!"
"""

turno = input('digite em que turno está, M-matutino ou V-Vespertino ou N- Noturno: ')
if turno == "m" or turno == "M":
    print('bom dia!')
elif turno == "v" or turno == "V":
    print('boa tarde!')
elif turno == "n" or turno == "N":
    print('boa noite!')
else:
    print('valor inválido!')
