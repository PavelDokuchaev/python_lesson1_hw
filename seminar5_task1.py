"""Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных свидетельствует
пустая строка."""

my_file = open('text.txt', 'w')
user_text = input('Напишите что-нибудь: ')
while user_text:
    my_file.writelines(user_text)
    user_text = input('Напишите что-нибудь: ')
    if not user_text:
        break
my_file.close()
my_file = open('text.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()

