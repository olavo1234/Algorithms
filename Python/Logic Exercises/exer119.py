import urllib
import urllib.error
import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está disbonivel no monento')
else:
    print('Consequi acessar o site pudim com sucesso')
