"""
ao inves de se limitar a herança e não usar
a herança multiplca(não sofrer o diamond problem)
a classe motor é instanciada na classe carro 
tendo como objeto motor nos seus atributos
"""

class Motor:
    def ligar(self):
        print('ligando o motor...')
    

    def desligar(self):
        print('desligando o motor...')


class Carro:
    def __init__(self) -> None:
        self.motor = Motor() # composição o carro tem um motor
    

    def ligar(self):
        self.motor.ligar()
        print('carro ligado')
    

    def desligar(self):
        self.motor.desligar()
        print('carro desligado')


if __name__ == '__main__':
    meuCarro = Carro()
    meuCarro.ligar()
