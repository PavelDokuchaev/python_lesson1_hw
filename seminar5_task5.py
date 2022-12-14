"""Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран."""


with open('sum.txt', 'w+') as f_obj:
    user_numbers = input('Введите числа через пробел: ')
    f_obj.writelines(user_numbers)
    user_numbers = user_numbers.split()
    sum_numbers = 0
    for el in user_numbers:
        sum_numbers += int(el)
    print(f'Сумма введенных чисел равна: {sum_numbers}')

