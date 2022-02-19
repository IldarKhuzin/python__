def int_func(text):
    """
    функция принимает слово маленькими буквами
    выводит слово с первой заглавной буквой
    :param text: слово из маленьких букв
    :return: слово из тех же букв, но первая буква заглавная
    """
    new_text = text.title()
    return new_text

text = input('введите слово')
print (int_func(text))
