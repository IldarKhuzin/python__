dig = 0
my_list = []
while dig == 0 :
    num = input('введите значение списка, для завершения ввода нажмите "Пробел" ')
    if num != ' ':
        my_list.append(num)
    else:
        break

for i in range(0,len(my_list)-1,2):
    mirror = my_list[i+1]
    my_list[i+1] = my_list[i]
    my_list[i] = mirror
print(my_list)
