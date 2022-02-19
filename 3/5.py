def str_split (a):
    """
    функция принимает строку из цифр или строку из цифр со словом "stop"
    возвращает сумму цифр и маркер слова "stop"
    :param a: строка из цифр или строка цифр со словом 'stop'
    :return: сумма цифр со словом 'stop', маркер слова "stop"
    """
    summa = 0
    stop = 0
    my_list = a.split(' ')
    for i in my_list:
        if i == 'stop':
            stop = 1
            break
        i = int(i)
        summa = summa + i
    return summa ,stop
my_sum = 0
stop = 0
while stop != 1:
    your_str = input('введите цифры, разделяя их пробелами, или введите слово "stop"')
    summa, stop = str_split(your_str)
    my_sum = my_sum + summa
    print(my_sum)
