"""Пользователь вводит целое положительное число. Найдите самую большую цифру
 в числе. Для решения используйте цикл while и арифметические операции."""

user_number = int(input('Введите целое положительное число: '))
max_digit = 0
while user_number > 0:
    current_digit = user_number % 10
    if current_digit > max_digit:
        max_digit = current_digit
    user_number //= 10
print(max_digit)


