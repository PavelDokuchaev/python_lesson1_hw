"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов"""


def my_func(arg_1, arg_2, arg_3):
    if arg_1 > arg_3 and arg_2 > arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_3 > arg_2:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3


arg_1 = int(input('Введите первое число: '))
arg_2 = int(input('Введите второе число: '))
arg_3 = int(input('Введите третье число: '))
my_sum = my_func(arg_1, arg_2, arg_3)
print(f'Сумма наибольших двух чисел из введенных равна: {my_sum}')
