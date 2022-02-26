# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.
with open('2test.txt') as file_obj:
    strings = file_obj.readlines()
    for i in range(len(strings)):
        word = str.split(strings[i],' ')
        print(f'количество слов в строке номер {i + 1} = {len(word)}')
    print(f'количество строк равно {len(strings)}')
