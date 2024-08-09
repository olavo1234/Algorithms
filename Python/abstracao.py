from abc import ABC, abstractmethod
from math import pi


"""
a abstração serve para impor um padrão 
na aplicação dos métodos e serve para
deixar o código limpo e facilitar
a manutenção do código
além de esconder a aplicação dos métodos deixando os
essas aplicações para as classes filhas
"""

class Figura(ABC):
    # ele vai receber a classe pai ABC
    # para ser uma classe abstrata 
    def __init__(self, cor) -> None:
        self.__cor = cor

# decorador para manuipular o atributo cor
    @property
    def cor(self):
        return self.__cor


    @cor.setter
    def cor(self, nova_cor):
        self.cor = nova_cor

# decorardor abstrato para definir esse método
    @abstractmethod
    def calcularArea(self):
        pass


# classe filho(subclass) circulo recebe como herança
# a classe pai abstrata apartir da herança
class Circulo(Figura):
    def __init__(self, cor, raio) -> None:
        super().__init__(cor)
        self.raio = raio


# se o método da classe abstrata for
# ignoada, retornará um error
    def calcularArea(self):
        return pi * (self.raio**2)


if __name__ == '__main__':
    c1 = Circulo('azul', 10)
    print(c1.calcularArea())
