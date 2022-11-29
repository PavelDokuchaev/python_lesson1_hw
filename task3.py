""" Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369. """

user_number = int(input('Введите число: '))
nn = 10 * user_number + user_number
nnn = 100 * user_number + nn
print(user_number + nn + nnn)
