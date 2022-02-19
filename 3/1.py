def do_div(first, second):
    """

    :param first: первый позиционный аргумент
    :param second: второй позиционный аргумент, отличный от нуля
    :return: результат деления первого аргумента на второй
    """
    if second == 0:
        return print('вы ввели недопустимый параметр')
    res = first/second
    return print(res)
first = int(input('введите первое число'))
second = int(input('введите второе число, отличное от нуля'))

do_div(first,second)
