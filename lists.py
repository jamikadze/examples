some_list = [12, 12.054, 'hello']
print(some_list)
print(len(some_list))
print(some_list[1])
another_list = some_list[:2]
some_list[2] = 'hi'
print(some_list)
new_list = some_list + another_list

# adding items
# new_list[5]='new item'
new_list.append('new item')
new_list.insert(0, 'start')

# Removing items
new_list.pop()  # удаляет последний
deleted_item = new_list.pop(-3)
deleted_item = new_list.remove(12)

print(new_list)
print(deleted_item)
number_list=[45,2,-74,55,9,-15]
number_list.sort()
q = number_list
print(number_list)
number_list.reverse()
print(number_list)