my_rating = [8,6,5,3,3,2]
new_el = int(input('введите новый элемент рейтинга'))
for i in range(len(my_rating)-1,-1,-1):
    if new_el <= my_rating[i]:
        my_rating.insert(i+1,new_el)
        break
if new_el > my_rating[0]:
    my_rating.insert(0,new_el)
print(my_rating)
