def person(name = None, surname = None, bdyear = None, town = None, email = None, phone = None):
    """

    :param name: name person
    :param surname: surname person
    :param bdyear: year of bird
    :param town: town
    :param email: email
    :param phone: phone
    :return: print pers info
    """
    pers = [name, surname, bdyear, town, email, phone]
    print(pers)

person('Ivan', 'Ivanov', 1999,'Moscow', 'ddfa@mad.jf', '223-322')
