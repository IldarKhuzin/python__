def string_to_digit(a):
    """
    функция принимает строку с цифрами и выводит только цифры
    - не более трехзначных чисел
    - не видит две отдельных цифры в конце
    :param a: строка с цифрами
    :return: список цифр
    """
    dig = 0
    digits = []
    i = 0
    while i < len(a) - 2:
        if a[i].isdigit():
            if a[i + 1].isdigit():
                if a[i + 2].isdigit():
                    dig = int(a[i] + a[i + 1] + a[i + 2])
                    digits.append(dig)
                    i += 3
                else:
                    dig = int(a[i] + a[i + 1])
                    digits.append(dig)
                    i += 2
            else:
                dig = int(a[i])
                digits.append(dig)
        i += 1
    return sum(digits)
print(string_to_digit('pos7u4etjhf8kjpuy7 lkjh'))