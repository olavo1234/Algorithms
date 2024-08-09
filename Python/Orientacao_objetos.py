# from datetime import datetime


# class Historico:
    
#     def __init__(self) -> None:
#         self.data_abertura = datetime.today()
#         self.transacoes = []


#     def imprime(self):
#         print(f'data abertura: {self.data_abertura}')
#         print('Transações: ')
#         for t in self.transacoes:
#             print("-", t)



# class Acesso:

#     def __init__(self, tipo) -> None:
#         self.classificacao = tipo
#         match self.classificacao:
#             case True:
#                 print('cliente com vip')
#             case False:
#                 print('cliente com acesso normal')
#             case _:
#                 print('impossivel ler tipo de cliente')



# class Cliente:

#     def __init__(self, nome, sobrenome, cpf) -> None:
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.cpf = cpf



# class Conta:

#     def __init__(self, numero, cliente, saldo, tipo=0, limite=1000.0) -> None:
#         self.numero = numero
#         self._titular = cliente 
#         self._saldo = saldo 
#         self.limite = limite
#         self.tipo_acesso = Acesso(tipo)
#         self.historico = Historico()


#     def get_saldo(self):
#         return self._saldo


#     def set_saldo(self, saldo):
#         self._saldo = saldo
    

#     def get_titular(self):
#         return self._saldo
    

#     def set_titular(self, titular):
#         self._titular = titular


#     def depositar(self, valor):
#         self._saldo += valor
#         self.historico.transacoes.append(
#             f"deposito de {valor}")


#     def sacar(self, valor):
#         if (self._saldo < valor):
#             print('impossivel fazer transação')
#         else:
#             self._saldo -= valor
#             self.historico.transacoes.append(
#                 f"saque de {valor}")


#     def transfere_para(self, destino, valor):
# # parâmetro destino será uma isntancia de objeto
#         retiro = self.sacar(valor)
#         if (retiro == False):
#             return False
#         else:
#             destino.depositar(valor)
#             self.historico.transacoes.append(
#                 f"transferência para {destino.titular.nome} "
#                 f"{destino.titular.sobrenome} de valor: {valor} ")
# # destino é uma variável que quarda 
# # o endereço do atributo valor de um objeto


#     def extrato(self):
#         print(f'numero: {self.numero}\nsaldo: {self.saldo}')
#         self.historico.transacoes.append(
#         f"tirou estrato - saldo de {self.saldo}")



# minha_conta = Conta('123.5', 'joão', 1000.0)
# minha_conta.depositar(100)
# print(minha_conta.pegar_saldo())










# # getter and setters e atributo de classes
# class Conta:
# # não iniciar no "__init__" porque
# # é a classe que vai controlar não o objeto
#     _total_contas = 0 # atributo da classe

#     def __init__(self, saldo) -> None:
#         self._saldo = saldo # saldo é um atributo de instancia
#         Conta._total_contas += 1


# # para encapsular é preciso utilizar o decorador
#     @staticmethod # método estático
#     # na função get é preciso do decorador para deixar
#     # a função sem argumento e funcionar
#     # tanto para o objeto instanciado tanto para a classe
#     def get_total_contas():
#         return Conta._total_contas

# # para não acessar um atributo encapsulado
# # diretamente utilizaremos métodos para modificalo
# # porém no python todos os atributos são públicos 
# # e o melhor jeito é utilizar o decorador properties
# # que torna mais limpo o uso do setter and getters 


#     def saldo(self):
#         return self._saldo
#     saldo = property(saldo)


# # getters and setters so podem ser 
# # incrementadas ser incrementadas por um real motivo   
#     @saldo.setter
#     def saldo(self, saldo):
#         if(saldo < 0):
#             print('saldo não pode ser negativo')
#         else:
#             self._saldo = saldo
# # o uso de getters and setters pode ser utilizado 
# # para incrementar uma valor lógica no atributo
# # get - pegar esse valor
# # set - para modifica-lo

# c1 = Conta(400)
# print(c1.get_total_contas())

# c2 = Conta(0)
# print(c2.get_total_contas())

# print(Conta.get_total_contas())







# # metodo de classe cls e classmethod 
# class Conta:
# # um metodo de classe diferente dos metodos estáticos
# # serve para definir um método que opera na classe
# # , e não em instancias

# # já os métodos estáticos utilizamos quando não
# # precisamos receber a referência de 
# # um objeto especial(seja da classe ou de uma instância)
# # e funciona como uma função comun, sem relação

#     _total_contas = 0

#     def __init__(self, saldo) -> None:
#         self.saldo = saldo
#         type(self)._total_contas += 1


#     @classmethod
#     # o uso do cls e do classmethod serve
#     # para alem do uso de instancia
#     # para acessar o valor e também adiciona
#     # a capacidade da propria classe
#     # ter o acesso dessed atributos 
#     def get_total_contas(cls):
#         return cls._total_contas


# c1 = Conta(100)
# print(c1.get_total_contas())

# c2 = Conta(10)
# print(c2.get_total_contas())

# print(Conta.get_total_contas())


















# class Conta:
# # o uso da variavel __slots__ serve para substituir o 
# # __dict__ sem assim evitando a implementação de
# # novos atributos na classe e além disso serve para 
# # ocupar menos memória ram  
#     __slots__ = ['_numero', '_titular', '_saldo', '_limite']
    
#     def __init__(self, numero, titular, saldo, limite=1000.0):
#         self._numero = numero
#         self._titular = titular
#         self._saldo = saldo
#         self._limite = limite


# conta = Conta('1-20', 'olavo', 100)

# # conta.nome = "minha_conta"

# # print(conta.nome)
# print(vars(conta))







# class Funcionario:
    
#     def __init__(self,nome,cpf,salario) -> None:
#         self._nome = nome
#         self._cpf = cpf
#         self._salario = salario


#     def trabalhar(self):
#         print('Trabalhando...')


#     def get_bonificacao(self):
#         return self._salario * 0.10


# class Gerente(Funcionario):

#     def __init__(self, nome, cpf, salario, senha, quant_pessoa) -> None:
#         super().__init__(nome, cpf, salario)
#         self._senha = senha 
#         self._total_gerenciados = quant_pessoa
    

#     def autenticar(self,senha):
#         if self._senha == senha:
#             print('Acesso permitido')
#             return True
#         else:
#             print('Acesso negado')
#             return False
    

#     def get_bonificacao(self):
#         # vai fazer chamar o conteudo do método
#         # para a classe e fazer a modificação 
#         return super().get_bonificacao() + 1000


# obje1 = Gerente('paulo','234.121.43.43.', 15000, 123, 40)

# obje2 = Funcionario('joão','456.344.654.654',1500)

# print(obje1._nome)
# print(obje2._nome)

# obje1.autenticar(123)
# obje1.trabalhar()
# print(obje1.get_bonificacao())
# print(obje2.get_bonificacao())


# método mágico __str__
# class Minha_classe:
    
#     def __str__(self) -> str:
#         return f'<Instância de {self.__class__.__name__}; endereço:{id(self)}>'

# mc = Minha_classe()

# print(mc)


# método mágico __repr__
# class Minha_classe():
#     pass

# if __name__ == '__main__':
#     mc = Minha_classe()
#     print(repr(mc))

# # o método __repr__ é normalmente utilizado com o eval()
# class Ponto:

#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
    

#     def __str__(self) -> str:
#         return f"({self.x},{self.y})"


#     def __repr__(self) -> str:
#         return f"Ponto({self.x + 1},{self.y + 1})"


# if __name__ == "__main__":
#     p1 = Ponto(1,2)
#     p2 = eval(repr(p1))

#     print(p1)
#     print(p2)


# verificar e manipular herança
# class Funcionario:
    
#     def __init__(self,nome,cpf,salario) -> None:
#         self._nome = nome
#         self._cpf = cpf
#         self._salario = salario


#     def trabalhar(self):
#         print('Trabalhando...')


#     def get_bonificacao(self):
#         return self._salario * 0.10


# class Gerente(Funcionario):

#     def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
#         super().__init__(cpf, nome, salario)
#         self._senha = senha
#         self._qtd_gerenciaveis = qtd_gerenciaveis


#     def get_bonificacao(self):
#         return super().get_bonificacao() + 1000


# class ControleDeFicacoes:

#     def __init__(self, total_bonificacao=0) -> None:
#         self._total_bonificacao = total_bonificacao


#     # def resgistra(self, obj):
#     #     if hasattr(obj, 'get_bonificacao'):
#     #         # o hasattr é uma função que recebe 2 parametros 
#     #         # o objeto e o atributo em formato de string
#     #         # e irá ver se esse atributo está no __dict__
#     #         self._total_bonificacao += obj.get_bonificacao()
#     #     else: 
#     #         print(
#     #             f'Instância de {self.__class__.__name__}'
#     #             f' não implementa o método get_bonificacao()'
#     #         )
        

#     def registra(self, obj):
#         # a maneira pythônica é usando o duck typing
#         # não iremos analisar o método
#         # mais sim pressupor a existêcia e
#         # tratar uma exeção caso ocorra
#         if isinstance(obj, Funcionario):
#             # analisa o tipo
#             self._total_bonificacao += obj.get_bonificacao()
#         else:
#             print(
#                 f'Instância de {self.__class__.__name__}'
#                 f' não implementa o método get_bonificacao()'
#             )


#     @property
#     def total_bonificacao(self):
#         return self._total_bonificacao


# class Cliente:

#     def __init__(self, nome, idade) -> None:
#         self.nome = nome
#         self.idade = idade


# if __name__ == '__main__':
#     funcionario = Funcionario('joão','111111111-1',2000)
#     print(f'bonificação funcionario: {funcionario.get_bonificacao()}')

#     gerente = Gerente("José", "222222222-22", 5000.0, '1234', 0)
#     print(f'bonificação gerente: {gerente.get_bonificacao()}')

#     controle = ControleDeFicacoes()
#     controle.registra(funcionario)
#     controle.registra(gerente)

#     print(f'total: {controle.total_bonificacao}')

#     cliente = Cliente('gustavo',10)
#     controle.registra(cliente)









# DUCK TYPING

# class Pato:
    
#     def grasna(self):
#         print('quack!')


# class Ganso:

#     def grasna(self):
#         print('quack!')


# if __name__ == '__main__':
#     pato = Pato()
#     pato.grasna()

#     ganso = Ganso()
#     ganso.grasna()







# herança e polimorfismo

# class Banco:

#     def __init__(self) -> None:
#         self._lista_conta = list()


#     def adiciona(self, conta):
#         self._lista_conta.append(conta)


#     def pegaConta(self, posicao):
#         return self._lista_conta[posicao]


#     def pegaTotalContas(self):
#         return len(self._lista_conta)



# class AtualizadorDeConta:

#     def __init__(self, selic, saldo_total=0) -> None:
#         self._selic = selic
#         self._saldo_total = saldo_total


#     def roda(self, conta):
#         try:
#             print(f"Saldo da Conta: {conta._saldo}")
#             self._saldo_total += conta.atualiza(self._selic)
#             print(f"Saldo Final: {self._saldo_total}")
#         except AttributeError:
#             print(
#                 f'ERROR: <Intância de {self.__class__.__name__}'
#                 f' não implementa o método {dir(Conta)[28]}()>'
#             )




# class Conta:
# # não iniciar no "__init__" porque
# # é a classe que vai controlar não o objeto
#     _total_contas = 0 # atributo da classe

#     def __init__(self, nome, numero, saldo) -> None:
#         self.titular = nome
#         self._numero_conta = numero
#         self._saldo = saldo # saldo é um atributo de instancia
#         Conta._total_contas += 1


#     def __str__(self) -> str:
#         return f"Dados da conta: \nsaldo: {self._saldo}\n... "


# # para encapsular é preciso utilizar o decorador
#     @staticmethod # método estático
#     # na função get é preciso do decorador para deixar
#     # a função sem argumento e funcionar
#     # tanto para o objeto instanciado tanto para a classe
#     def get_total_contas():
#         return Conta._total_contas

# # para não acessar um atributo encapsulado
# # diretamente utilizaremos métodos para modificalo
# # porém no python todos os atributos são públicos 
# # e o melhor jeito é utilizar o decorador properties
# # que torna mais limpo o uso do setter and getters 


#     def saldo(self):
#         return self._saldo
#     saldo = property(saldo)


# # getters and setters so podem ser 
# # incrementadas ser incrementadas por um real motivo   
#     # @saldo.setter
#     # def saldo(self, saldo):
#     #     if(saldo < 0):
#     #         print('saldo não pode ser negativo')
#     #     else:
#     #         self._saldo = saldo
# # o uso de getters and setters pode ser utilizado 
# # para incrementar uma valor lógica no atributo
# # get - pegar esse valor
# # set - para modifica-lo


#     def deposita(self, valor):
#         self._saldo += valor
    

#     def atualiza(self, taxa):
#         self._saldo += self._saldo * taxa
#         return self._saldo


# class ContaCorrente(Conta):

#     def __init__(self, saldo) -> None:
#         super().__init__(saldo)


#     def atualiza(self, taxa):
#         # reescrever o método 
#         # self._saldo += self._saldo * (taxa*2)
#         # return self._saldo
#         return super().atualiza(taxa*2)


#     def deposita(self, valor):
#         # ele vai pegar o método do super classe
#         # (classe mâe) e modificar para que somente
#         # o método deposito da classe ContaCorrente
#         # sofra essa alteração
#         return super().deposita(valor - 0.10)


# class ContaPoupanca(Conta):

#     def __init__(self, saldo) -> None:
#         super().__init__(saldo)


#     def atualiza(self, taxa):
#         return super().atualiza(taxa*3)


# class ContaInvestimento(Conta):
    
#     def __init__(self, nome, numero, saldo) -> None:
#         super().__init__(nome, numero, saldo)
#         self.nome_titulo = list()


#     def atualiza(self, alavancagem=0):
#         self._saldo += alavancagem
#         return self._saldo



# class Teste:
    
#     def __init__(self, verificarTeste) -> None:
#         self.chamarTeste = verificarTeste


# # if __name__ == '__main__':
# #     c1 = Conta('pedro','12-4',1000)
# #     c2 = Conta('gustavo','42-0',300)
# #     c3 = Conta('jorge','18-4',900)
# #     c4 = Conta('joão','14-8',2000)
# #     atualizaCont = AtualizadorDeConta(8.1) 
# #     banco = Banco()
# #     banco.adiciona(c1)
# #     banco.adiciona(c2)
# #     banco.adiciona(c3)
# #     banco.adiciona(c4)
# #     for c in range(0, banco.pegaTotalContas()):
# #         atualizaCont.roda(banco.pegaConta(c))


# if __name__ == '__main__':
#     conta = Conta('joão,', '23-1', 1550)
#     testeObj = Teste('testarAgora')
#     atualizarCont = AtualizadorDeConta(8)
#     atualizarCont.roda(testeObj)

#     print('passou')









# classes abstratas
# import abc

# class Funcionario(abc.ABC):

#     def __init__(self, nome, cpf, salario=0) -> None:
#         self.nome = nome
#         self.cpf = cpf
#         self.salario = salario
    
#     @abc.abstractmethod
#     def get_bonificacao(self):
#         pass


# class ControleDeBonificacoes:

#     def __init__(self, total_bonifinicacoes=0) -> None:
#         self.__total_bonificacoes = total_bonifinicacoes
    

#     def registra(self, obj):
#         if(hasattr(obj, 'get_bonificacao')):
#             self.__total_bonificacoes += obj.get_bonificacao()
#         else:
#             print(
#                 f'Instância de {self.__class__.__name__}' 
#                 'não implementa o método get_bonificacao()'
#             )


# class Gerente(Funcionario):

#     def __init__(self, nome, cpf, salario=0) -> None:
#         super().__init__(nome, cpf, salario)
    

#     def get_bonificacao(self):
#         return self.salario * 0.15



# class Diretor(Funcionario):

#     def __init__(self, nome, cpf, salario=0) -> None:
#         super().__init__(nome, cpf, salario)


# if __name__ == '__main__':
#     gerente = Gerente('jose', '2222222222-2', 5000)
#     diretor = Diretor('joão', '1111111111-1', 10000) 
#     print(gerente.get_bonificacao())




# import abc

# class Conta(abc.ABC):

#     def __init__(self, numero, titular, saldo=0, limite=10000.0) -> None:
#         self._numero = numero
#         self._titular = titular
#         self._saldo = saldo
#         self._limite = limite


#     @abc.abstractmethod
#     def atualiza():
#         pass



# class ContaCorrente(Conta):

#     def __init__(self, numero, titular, saldo) -> None:
#         super().__init__(numero, titular, saldo)
#         self.tipo = 'Corrente'
    

#     def __str__(self) -> str:
#         return f'Tipo: {self.tipo}'


#     def atualiza(self, taxa):
#         # reescrever o método 
#         # self._saldo += self._saldo * (taxa*2)
#         # return self._saldo
#         self._saldo += self._saldo * (taxa*2)
#         return self._saldo


#     def deposita(self, valor):
#         self._saldo + valor - 0.10



# class ContaPoupanca(Conta):

#     def __init__(self,numero, titular, saldo) -> None:
#         super().__init__(numero, titular, saldo)
#         self.tipo = 'Poupança'


#     def __str__(self) -> str:
#         return f'Tipo: {self.tipo}'


#     def atualiza(self, taxa):
#         self._saldo += self._saldo * (taxa*3)
#         return self._saldo



# class ContaInvestimento(Conta):
    
#     def __init__(self, nome, numero, saldo) -> None:
#         super().__init__(nome, numero, saldo)
#         self.nome_titulo = list()
#         self.tipo = 'Investimento'


#     def __str__(self) -> str:
#         return f'Tipo: {self.tipo}'


#     def atualiza(self, alavancagem=0):
#         self._saldo += alavancagem
#         return self._saldo



# if __name__ == '__main__':
#     cc = ContaCorrente('112-1','jose',1000)
#     cp = ContaPoupanca('321-1','joão',1000)
#     ci = ContaInvestimento('12-1','maria',1000)

#     cc.atualiza(0.01)
#     cp.atualiza(0.01)
#     ci.atualiza(1000)

#     print(cc._saldo)
#     print(cp._saldo)
#     print(ci._saldo)

#     print(cp)






# herança multipla e interfaces
# class Funcionario():

#     def __init__(self, nome, cpf, salario=0) -> None:
#         self.nome = nome
#         self.cpf = cpf
#         self.salario = salario


#     def get_bonificacao(self):
#         pass



# class AutenticavelMixIn:
# essa classe é dada por um MixIn
# por ser uma classe não indepedente

#     def autenticar(self, senha):
#         if self._senha == senha:
#             print('Senha correta')
#             return True
#         else:
#             print('Senha incorreta')
#             return False



# class ControleDeBonificacoes:

#     def __init__(self, total_bonifinicacoes=0) -> None:
#         self.__total_bonificacoes = total_bonifinicacoes
    

#     def registra(self, obj):
#         if(hasattr(obj, 'get_bonificacao')):
#             self.__total_bonificacoes += obj.get_bonificacao()
#         else:
#             print(
#                 f'Instância de {self.__class__.__name__}' 
#                 'não implementa o método get_bonificacao()'
#             )


# class Gerente(Funcionario, Autenticavel):

#     def __init__(self, nome, cpf, salario=0, senha=0, quant_pessoa=0) -> None:
#         super().__init__(nome, cpf, salario)
#         self._senha = senha
#         self.quant_pessoa = quant_pessoa


#     def get_bonificacao(self):
#         return self.salario * 0.15



# class Diretor(Funcionario, Autenticavel):

#     def __init__(self, nome, cpf, salario=0, senha=0, quant_pessoa=0) -> None:
#         super().__init__(nome, cpf, salario)
#         self._senha = senha
#         self.quant_pessoa = quant_pessoa



# class SistemaInterno:
    
#     def login(self, obj):
#         if hasattr(obj, 'autenticar'):
#             return True
#         else:
#             print(f'{obj.__class__.__name__} não é autenticável')
#             return False


# class Cliente():

#     def __init__(self, nome, cpf, senha) -> None:
#         self._nome = nome
#         self._cpf = cpf
#         self._senha = senha



# if __name__ == '__main__':
#     diretor = Diretor('João', '111111111-11', 3000.0, '1234')
#     gerente = Gerente('José', '222222222-22', 5000.0, '1235')
#     cliente = Cliente('Maria', '333333333-33', '1236')

#     sistema = SistemaInterno()
#     print(sistema.login(diretor))
#     sistema.login(gerente)
#     print(sistema.login(cliente))





# problema do diamante 
# se as classes B e C herdarem a classe A e a classe D 
# herdar as classes B e C, e as classes B e C têm um 
# método m2(), qual método a classe D herda?


# class A:

#     def m1(self):
#         print('método de A')



# class B(A):

#     def m1(self):
#         return super().m1()


#     def m2(self):
#         print('método de B')



# class C(A):

#     def m1(self):
#         return super().m1()


#     def m2(self):
#         print('método de C')



# class D(B, C):
    
#     def m1(self):
#         return super().m1()


#     def m2(self):
#         return super().m2()



# if __name__ == '__main__':
#     obj = D()
#     obj.m2()
#     print(D.mro())
#     # o método mágico __mro__ presente na classe
#     # method resolution order que percorre a
#     # hierarquia de classes






# mix-ins
# são classes que não possui uma indepedencia


# e podemos misturá-las nas classes de nosso sistema

# class Funcionario:
#     pass

# class Gerente(Funcionario, AutenticavelMixIn, HoraExtraMixIn):
#     pass

# class Cliente(AutenticavelMixIn):
#     pass

# class Escrituraria(Funcionario, AutenticavelMixIn):
#     pass

# import math

# class AutenticavelMixIn:

#     def autentica(self, senha):
#         if self._senha == senha:
#             print('Senha correta')
#             return True
#         else:
#             print('Senha incorreta')
#             return False




# class AtendimentoMixIn:

#     def __init__(self) -> None:
#         self._dadosCliente = list()
#         self._cadastroTotal = list()


#     def atende_cliente(self, nome, sobrenome, cpf):
#         # o cadatro de um novo cliente so será salvo
#         # se utilizar o método cadastro_atendimento
#         self._dadosCliente.append(nome)
#         self._dadosCliente.append(sobrenome)
#         self._dadosCliente.append(cpf)


#     def cadastro_atendimento(self):
#         listaCadastro = self._dadosCliente[:]
#         self._cadastroTotal.append(listaCadastro)
#         self._dadosCliente.clear()


#     def get_cadastro(self):
#         for i, c in enumerate(self._cadastroTotal):
#             print(f'cliente nº: {i+1}')
#             print(c)
#             print()




# class HoraExtraMixIn:

#     def calcular_hora_extra(self, quant_hora_extra, salario=0, horas=0):
#         valor_hora = salario / horas
#         valor_hora_ext = valor_hora + (valor_hora / 100) * 50
#         total = valor_hora_ext * quant_hora_extra
#         return f'{total:.2f}'



# class Funcionario():

#     def __init__(self, nome, cpf, salario=0, horas_trab=0) -> None:
#         self.nome = nome
#         self.cpf = cpf
#         self.salario = salario
#         self.horas_trab = horas_trab


#     def get_bonificacao(self):
#         pass



# class ControleDeBonificacoes:

#     def __init__(self, total_bonifinicacoes=0) -> None:
#         self.__total_bonificacoes = total_bonifinicacoes
    

#     def registra(self, obj):
#         if(hasattr(obj, 'get_bonificacao')):
#             self.__total_bonificacoes += obj.get_bonificacao()
#         else:
#             print(
#                 f'Instância de {self.__class__.__name__}' 
#                 'não implementa o método get_bonificacao()'
#             )



# class Gerente(Funcionario, AutenticavelMixIn, HoraExtraMixIn):

#     def __init__(self, nome, cpf, salario=0, senha=0, quant_pessoa=0, horas_trab=0) -> None:
#         super().__init__(nome, cpf, salario, horas_trab)
#         self._senha = senha
#         self.quant_pessoa = quant_pessoa


#     def get_bonificacao(self):
#         return self.salario * 0.15



# class Diretor(Funcionario, AutenticavelMixIn):

#     def __init__(self, nome, cpf, salario=0, senha=0, quant_pessoa=0, horas_trab=0) -> None:
#         super().__init__(nome, cpf, salario, horas_trab)
#         self._senha = senha
#         self.quant_pessoa = quant_pessoa



# class SistemaInterno:
    
#     def login(self, obj):
#         if hasattr(obj, 'autenticar'):
#             return True
#         else:
#             print(f'{obj.__class__.__name__} não é autenticável')
#             return False



# class Cliente(AutenticavelMixIn):

#     def __init__(self, nome, cpf, senha) -> None:
#         self._nome = nome
#         self._cpf = cpf
#         self._senha = senha



# class Escrituraria(Funcionario, AutenticavelMixIn):
    
#     def __init__(self, nome, cpf, salario=0, horas_trab=0) -> None:
#         super().__init__(nome, cpf, salario, horas_trab)
#         self.fazerAtendimento = AtendimentoMixIn()



# if __name__ == '__main__':
#     # escrituraria = Escrituraria('joão', '100.234.123.76', 11.344)
    
#     # escrituraria.fazerAtendimento.atende_cliente('joão', 'marcelo', '123.123.123.12')
#     # escrituraria.fazerAtendimento.cadastro_atendimento()
    
#     # escrituraria.fazerAtendimento.atende_cliente('pedro', 'barcelos', '456.245.123.87')
#     # escrituraria.fazerAtendimento.cadastro_atendimento()
    
#     # escrituraria.fazerAtendimento.atende_cliente('jose', 'xicara', '345.656.455.22')
#     # escrituraria.fazerAtendimento.cadastro_atendimento()

#     # escrituraria.fazerAtendimento.get_cadastro()

#     gerente = Gerente('jorge', '123.123.234.12', 12000, 122, 10, 220)

#     print(gerente.calcular_hora_extra(5, gerente.salario, gerente.horas_trab))



# 
# em outro arquivo (manipulador.py)

# class ManipuladorDeTributaveis:

#     def calcula_imposto(self, lista_tributaveis):
#         total = 0
#         for t in lista_tributaveis:
#             total += t.get_valor_imposto()
        
#         return total


# # 


# import abc

# class tributavelMixIn:

#     def get_valor_imposto(self):
#         pass




# class SeguroDeVida(tributavelMixIn):

#     def __init__(self, valor, titular, numero_apolice) -> None:
#         self._valor = valor
#         self._titular = titular
#         self._numero_apolice = numero_apolice


#     def get_valor_imposto(self):
#         return 50 + self._valor * 0.05



# class Conta(abc.ABC):

#     def __init__(self, numero, titular, saldo=0, limite=10000.0) -> None:
#         self._numero = numero
#         self._titular = titular
#         self._saldo = saldo
#         self._limite = limite


#     @abc.abstractmethod
#     def atualiza():
#         pass



# class ContaCorrente(Conta, tributavelMixIn):

#     def __init__(self, numero, titular, saldo) -> None:
#         super().__init__(numero, titular, saldo)
#         self.tipo = 'Corrente'
    

#     def __str__(self) -> str:
#         return f'Tipo: {self.tipo}'
    

#     def get_valor_imposto(self):
#         return self._saldo * 0.01


#     def atualiza(self, taxa):
#         # reescrever o método 
#         # self._saldo += self._saldo * (taxa*2)
#         # return self._saldo
#         self._saldo += self._saldo * (taxa*2)
#         return self._saldo


#     def deposita(self, valor):
#         self._saldo + valor - 0.10



# class ContaPoupanca(Conta):

#     def __init__(self,numero, titular, saldo) -> None:
#         super().__init__(numero, titular, saldo)
#         self.tipo = 'Poupança'


#     def __str__(self) -> str:
#         return f'Tipo: {self.tipo}'


#     def atualiza(self, taxa):
#         self._saldo += self._saldo * (taxa*3)
#         return self._saldo



# class ContaInvestimento(Conta):
    
#     def __init__(self, nome, numero, saldo) -> None:
#         super().__init__(nome, numero, saldo)
#         self.nome_titulo = list()
#         self.tipo = 'Investimento'


#     def __str__(self) -> str:
#         return f'Tipo: {self.tipo}'


#     def atualiza(self, alavancagem=0):
#         self._saldo += alavancagem
#         return self._saldo



# if __name__ == '__main__':
#     cc1 = ContaCorrente('112-1','jose',1000)
#     cc2 = ContaCorrente('167-2','joao',2000)

#     # cp = ContaPoupanca('321-1','joão',1000)
#     # ci = ContaInvestimento('12-1','maria',    

#     seguro1 = SeguroDeVida(100, 'jose', '341-11')
#     seguro2 = SeguroDeVida(200, 'maria', '344-32')

#     lista_tributaveis = list()
#     lista_tributaveis.append(cc1)
#     lista_tributaveis.append(cc2)
#     lista_tributaveis.append(seguro1)
#     lista_tributaveis.append(seguro2)

#     manipulador = ManipuladorDeTributaveis()
#     total = manipulador.calcula_imposto(lista_tributaveis)

#     print(total)








# Interfaces

# interfaces utilizando o método abc é uma solução
# mais elegante do que so mix-ins

import abc

class Autenticavel(abc.ABC):
    """ Classe abstrata que contém operações de um objeto autenticável 
    
    As subclasses concretas devem sobrescrever o método autentica
    """


    @abc.abstractmethod
    def autenticar(self, senha):
        """ Método abstrato que faz a verificação da senha
        devolve True se a senha confere, e False caso contrário 
        """
        pass



class Gerente():

    def __init__(self, nome, cpf, salario=0, senha=0, quant_pessoa=0, horas_trab=0) -> None:
        # super().__init__(nome, cpf, salario, horas_trab)
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self._senha = senha
        self.quant_pessoa = quant_pessoa


    def get_bonificacao(self):
        return self.salario * 0.15



class Diretor():

    def __init__(self, nome, cpf, salario=0, senha=0, quant_pessoa=0, horas_trab=0) -> None:
        # super().__init__(nome, cpf, salario, horas_trab)
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.senha = senha
        self.quant_pessoa = quant_pessoa



if __name__ == '__main__':
    # Autenticavel.register(Gerente)
    # # com o método register das ABCs introduzem uma subclasse
    # # virtual que são classes que não herdam de uma classe mas são
    # # reconhecidas pelos métodos isinstance e issubclass 

    # gerente = Gerente('joão',' 111111111.11', 3000)
    # # ao fazer o register de gerente o python não vai 
    # # verificar a implementação do método autenticar,
    # # ele vai sequir se apenas a interface for iqual a
    # # class Autenticavel  

    # gerente.autenticar('??')
    # # quando chamamos o método inexistente 
    # # o python lançará uma exceção

    # print(isinstance(gerente, Autenticavel))
    # print(issubclass(Gerente, Autenticavel))


    # Autenticavel.register(Diretor)

    # d = Diretor('josé', '222222222.22', 30000)

    # if isinstance(d, Autenticavel):
    #     d.autenticar('?')
    # else:
    #     print('diretor não implementa a interface Autenticavel')


    class SistemaInterno:

        def login(self, obj):
            if isinstance(obj, Autenticavel):
                obj.autenticar(obj._senha)
                return True
            else:
                print(
                    f'{obj.__class__.__name} não é autenticavel'
                    )
                return False
