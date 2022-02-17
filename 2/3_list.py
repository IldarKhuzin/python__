my_list = ['весна','лето','осень','зима']
month = int(input('введите номер месяца '))
if month > 2 and month < 6:
    print(my_list[0])
elif month > 5 and month < 9:
    print(my_list[1])
elif month > 8 and month < 12:
    print(my_list[2])
else:
    print(my_list[3])
