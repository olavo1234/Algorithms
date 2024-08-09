class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada) -> None:
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0
        self.__salario = 0


    @property
    def salario(self):
        return self.__salario


    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("impossivel alterar diretamente. use acalcular_salario().")


    def registra_hora_trabalhada(self):
        self.horas_trabalhadas += 1


    def calcular_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada


pedro = Funcionario("pedro", "gerente de vendas", 50)
pedro.salario = 1000000
