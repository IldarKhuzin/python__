def int_func(text):
    """
    функция принимает слово маленькими буквами
    выводит слово с первой заглавной буквой
    :param text: слово из маленьких букв
    :return: слово из тех же букв, но первая буква заглавная
    """
    new_text = text.title()
    return new_text

some_text = input('введите текст из маленьких букв')
some_text = str.split(some_text,' ')
new_text = []
for i in some_text:
    new_text.append(int_func(i))
delimeter = ' '
new_string = ' '.join(new_text)
print(new_string)