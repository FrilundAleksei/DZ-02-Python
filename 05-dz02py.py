# Реализовать алгоритм перемешивания списка.

import random
# lst = [random.randint(-20,50) for i in range(random.randint(-20,50))]
# print(f"Исходный список:\n {lst}")
# random.shuffle(lst)
# print(f"Список после перемешивания:\n {lst}")


#Длиннее но мне так больше нравтся

def list_first(n, lft, rght):
    return [random.randint(lft, rght) for i in range(n)]

def list_second(lst):
    return random.shuffle(lst)

n = int(input('Количество элементов списка: '))
lft = int(input('Граница 1 диапазона значений элементов списка: '))
rght = int(input('Граница 2 диапазона значений элементов списка: '))

mylist = list_first(n, lft, rght)
print(f"Исходный список: \n {mylist}")
list_second(mylist)
print(f"Список после перемешивания:\n {mylist}")

# да, не предусмотренны случаи ошибочнойго ввода, или ввода сначала большей, а затем меньшей границы списка. Но алгоритм перемешевания работает ))