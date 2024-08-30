"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).

passos 
ler e entender o que se esta sendo pedido junto com os calculos 
pedir ao usuario o tamanho do arquivo para dowload em MB e a velocidade de um link da internet em Mbps
quardar o valor de  MB e Mbps 
e calcular (MB)/(Mbps/8)
e transformar de segundos para mimutos 
declarando uma variavel multiplicado por 60
e exibir na tela o resultado

os 5Qs
amanho do arquivo para dowload em MB e a velocidade de um link da internet em Mbps
calcular e informar o tempo do dowload do arquivo em minutos
devo dividir o numero somente por 8
informa em minutos o tempo aproximado de dowload 
5

MB = float input"informe o tamanho do arquivo em MB: "
mbps = float input"informe a velocidade da internet em Mbps: "
tempo = MB / (mbps / 8)
minutos = tempo // 60
print"minutos"

"""
mb = float(input('informe o tamanho do arquivo em MB: '))
mbps = float(input('informe a velocidade da internet em Mbps: '))
tempo = mb / (mbps / 8)
minutos = tempo // 60
segundos = tempo % 60

print(

    f'com o tamanho do arquivo de {mb} MB\n'
    f'e com a velocidade de internet de {mbps} Mbps\n'
    f'o tempo é de {segundos:.0f}segundos e de minutos é {minutos:.0f}'

)
