# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
# виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:

    def __init__(self,data_string):
        self.data_string = str(data_string)

    @classmethod
    def string_to_number(cls, data_string):
        my_data = []
        for i in data_string.split():
            if str.isdigit(i):
                my_data.append(int(i))
        return my_data

    @staticmethod
    def is_valid(my_string):
        if my_string [0] <= 0 or my_string[0]> 31:
            return f'введен некорректный день'
        if my_string[1] <= 0 or my_string[1] >12:
            return f'введен некорректный месяц'
        return f'вы ввели корректную дату'


print(Data.string_to_number('05 - 09 - 1975'))
print(Data.is_valid(Data.string_to_number('4 - 0 - 1954')))
print(Data.is_valid(Data.string_to_number('34 - 10 - 1954')))
print(Data.is_valid(Data.string_to_number('4 - 10 - 1954')))


