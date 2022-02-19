def my_func(a,b,c):
    """
    :param a: число
    :param b: число
    :param c: число
    :return: сумма двух наибольших чисел
    """
    data = [a,b,c]
    res = sorted(data)
    sum_of_two = res[2]+res[1]
    return sum_of_two
print(my_func(7,37,444))
