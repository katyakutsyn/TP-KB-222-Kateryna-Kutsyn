
my_list = []

# extend(використовується для додавання всіх елементів із іншого списку)
my_list.extend([1, 2, 3])
print("extend():", my_list)

# append(додає заданий елемент в кінець спику)
my_list.append(4)
print("append():", my_list)

# insert(вставляє заданий елемент (val) на позицію з вказаним індексом (id) у списку.)
my_list.insert(1, 5)
print("insert(1, 5):", my_list)

# remove(видаляє перший елемент зі спику який має задане значення val)
my_list.remove(3)
print("remove(3):", my_list)

# clear( видалення всіх елементів із спискую)
my_list.clear()
print("clear():", my_list)

# sort(сортує елементи списку в порядку зростання)
my_list = [4, 2, 1, 3]
my_list.sort()
print("sort():", my_list)

# reverse(змінює порядок елементів у списку на протилежний ))
my_list.reverse()
print("reverse():", my_list)

# copy( створює та повертає копію поточного списку)
copied_list = my_list.copy()
print("copy():", copied_list)
