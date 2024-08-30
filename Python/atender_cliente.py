"""Problema: Atendendo clientes em uma Fila

Você está implementando um sistema de atendimento para uma loja.
A loja tem uma fila de clientes que estão esperando para ser atendidos.
Cada cliente tem um nome e uma prioridade de atendimento. 
clientes com prioridade alta devem ser atendidos antes dos clientes 
com prioridade baixa. Se dois clientes têm a mesma 
prioridade, eles são atendidos na ordem em que chegaram.


Implementar uma classe cli que tenha os atributos nome e prioridade.
Implementar uma classe FilaDeclis que gerencie a fila de clis, com métodos para:

    Adicionar um cli à fila (adicionar_cli).
    Atender o próximo cli na fila, de acordo com a prioridade (atender_cli).
    Mostrar a fila atual (mostrar_fila).
"""

from typing import List, Any



class Cliente:

    def __init__(self, nome, prioridade) -> None:
        self.nome = nome
        self.prioridade = prioridade
    
    
    def __repr__(self) -> str:
        return f'Name: {self.nome}, Priority: {self.prioridade}'
    


class FilaDeClientes:
    
    def __init__(self) -> None:
        self.fila: List[Any] = []
    


    def adicionarCliente(self, cliente: Cliente) -> None:
        while True:
            if not self.fila:
                self.fila.append(cliente)
                break
            else:
                for c in self.fila:
                    if c.prioridade <= cliente.prioridade:
                        self.fila.insert(self.fila.index(c), cliente)
                        break
                    if cliente.prioridade >= c.prioridade :
                        self.fila.insert(self.fila.index(c) + 1, cliente)
                        break
            break



    def atenderClinete(self) -> Any:
        if not self.fila:
            raise IndexError('Fila vazia')
        
        return self.fila.pop(0) 


    def mostrar(self) -> None:
        for cliente in self.fila:
            print(cliente) 
