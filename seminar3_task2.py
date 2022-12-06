"""Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def info_func(name, surname, birthday, city, email, phone):
    print(f'Имя: {name}; \nФамилия: {surname}; \nГод рождения: {birthday};'
          f' \nГород проживания: {city}; \nemail: {email}: \nТелефон: {phone}')


user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_birthday = int(input('Введите год рождения: '))
user_city = input('Введите город проживания: ')
user_email = input('email: ')
user_phone = int(input('Введите номер телефона: '))

info_func(name=user_name, surname=user_surname, birthday=user_birthday,
          city=user_city, email=user_email, phone=user_phone)
