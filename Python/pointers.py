# imutaveis
a = 10
b = a
a = 20
print(a)
print(b)


# mutaveis
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)
print(list2)


def modify_lits(lst):
    # lst é uma referência para a lista
    lst.append(4)


my_list = [1, 2, 3]
modify_lits(my_list)
print(my_list)


class MyClass:
    pass


my_class = MyClass()

print(my_class)
# Vai imprimir o enderecamento do objeto 
print(MyClass)
