# plimorfismo significa multiplas formas
# do grego poli=muitas, morphos=formas

class Super:
    def hello(self):
        print('Olá, eu sou a Superclass')
    

class Sub(Super):
    def hello(self):
        print('Olá, eu sou a Subclass')
    

class Subsub(Sub):
    def hello(self):
        print('Olá, eu sou a Subsubclass')
    

obj = Subsub()
obj.hello()


"""
os métodos são iquais mas executam diferentes comandos
a abstração feita com o modulo abc e com o decorador abstractmethod
é um exemplo de uso de polimorfismo  
"""

from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def desenhe(self):
        pass



class Quadrado(Figura):
    def desenhe(self):
        print('desenhando um quadrado...')


class Circulo(Figura):
    def desenhe(self):
        print('desenhando um circulo...')


f1 = Quadrado()
f2 = Circulo()

f1.desenhe()
f2.desenhe()
