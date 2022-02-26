# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

str_u = input('введите строку')
next_line = '\n'
str_user = str_u + next_line
while str_u != '':
    with open ('1test.txt', 'a') as file_obj:
        file_obj.write(str_user)
    str_u = input('введите строку')
    next_line = '\n'
    str_user = str_u + next_line



