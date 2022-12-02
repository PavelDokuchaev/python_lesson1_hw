"""Для списка реализовать обмен значений соседних элементов, т.е. значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input()."""

my_list = []
length_list = int(input('Введите количество элементов списка: '))
for i in range(length_list):
    new_element = input(f'Введите {i} элемент списка: ')
    my_list.append(new_element)
print(f'Заданный список: {my_list}')
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        list_el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = list_el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        list_el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = list_el
        i += 2
print(f'Список с реализованным обменом значений соседних элементов: {my_list}')




