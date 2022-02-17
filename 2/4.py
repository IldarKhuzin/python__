my_string = input('введите несколько слов через пробел')
my_list = str.split(my_string)
for i in range(len(my_list)):
    print(i+1,my_list[i][:10])
