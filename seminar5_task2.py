"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

my_file = open('hokku.txt', 'r')
content = my_file.read()
print(content)
my_file.close()
with open('hokku.txt') as f_obj:
    count = 0
    for line in f_obj:
        count += 1
    print(f'Количество строк в хокку: {count}')
with open('hokku.txt', 'r') as f_obj:
    for line in f_obj:
        line = line.split()
        print(f'В строке: {line}')
        count = 0
        for el in line:
            count += 1
        print(f'Количество слов: {count}')









