# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

my_string = input('введите цифры через пробел')  # запрашиваем у пользователя строку
with open('5test.txt', 'w') as file_obj:
    file_obj.write(my_string)                    # записываем её в файл

with open('5test.txt') as file_obj:
    content = file_obj.readline()                # считываем строку из файла
    digits = str.split(content)                  # разбиваем на элементы через пробел
    dig_sum = 0
    for i in range(len(digits)):
        dig_sum = dig_sum + int(digits[i])       # переводим в int и суммируем
    print(dig_sum)

