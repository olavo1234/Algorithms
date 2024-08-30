"""Problema: Gerenciamento de Tarefas

Você está desenvolvendo um sistema de gerenciamento de tarefas.
Cada tarefa tem um título e uma descrição. 
O sistema deve permitir que o usuário adicione,
remova e exiba todas as tarefas em uma lista ligada.

Requisitos:

    Adicionar Tarefa: Deve ser possível adicionar uma nova tarefa ao final da lista.
    Remover Tarefa: Deve ser possível remover uma tarefa pelo título.
    Exibir Tarefas: Deve ser possível exibir todas as tarefas na lista.
    Contar Tarefas: Deve ser possível contar quantas tarefas estão na lista.

"""

class Tarefa:
    
    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description
        self.next = None


    def get_title(self):
        return self.title


    def get_next(self):
        return self.next
    

    def get_description(self):
        return self.description


    def set_title(self, new_title):
        self.title = new_title


    def set_next(self, new_next):
        self.next = new_next


    def set_description(self, new_description):
        self.description = new_description



class LinkedList:

    def __init__(self) -> None:
        self.head = None


    def adicionar_tarefa(self, title, description):
        new_tarefa = Tarefa(title, description)

        if not self.head:
            self.head = new_tarefa
            return
        
        current = self.head

        while current.get_next():

            current = current.get_next()
        
        current.set_next(new_tarefa)
    
        return new_tarefa


    def remover_tarefa(self, title):
        current = self.head
        found = False
        previous = None

        while not found:

            if current.get_title() == title:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


    def is_empty(self):
        return self.head == None


    def exibir_tarefa(self):
        current = self.head

        while current:

            print(current.get_title())

            current = current.get_next()


    def contar_tarefa(self):

        current = self.head
        cont = 0 

        while current:
            cont += 1 
            current = current.get_next()
        
        return cont


    def place_in_list(self):
        current = self.head
        lst = []

        while current:
            lst.append(current.get_title())
            current = current.get_next()
        return lst



gerenciador = LinkedList()


gerenciador.adicionar_tarefa("Estudar Python", "Estudar listas ligadas em Python")
gerenciador.adicionar_tarefa("Estudar Python", "Estudar listas ligadas em Python")
gerenciador.adicionar_tarefa("Estudar Python", "Estudar listas ligadas em Python")

gerenciador.exibir_tarefa()

print(gerenciador.place_in_list())
gerenciador.remover_tarefa("Estudar Python")


gerenciador.exibir_tarefa()
