# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее. Подсказка: используйте функцию
# count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа, начиная с 3.
# # При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
# # повторение элементов списка прекратится.

# итератор с помощью count
from itertools import count, cycle
start = int(input('введите начальную цифру'))
end = int(input('введите конечную цифру'))
my_count = count(start,1)
print('count')
for i in my_count:
    if i > end:
        break
    print (i)

# итератор с помощью cycle

my_list = [1,2,3,4,5,6,7,8,9,0]
my_cicle = cycle(my_list)
print('cycle ')
i = 0
for _ in my_cicle:
    print(_)
    i += 1
    if i > 10:
        break

