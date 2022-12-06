"""Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль."""


def dividing_numbers(arg_1, arg_2):
    try:
        res = arg_1 / arg_2
        return res
    except ZeroDivisionError:
        return 'Делить на ноль нельзя'
    except ValueError:
        return


user_number_1 = int(input('Введите делимое: '))
user_number_2 = int(input('Введите делитель: '))
print(f'{user_number_1} / {user_number_2} = '
      f'{dividing_numbers(user_number_1, user_number_2)}')
