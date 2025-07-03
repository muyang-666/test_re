my_list = [3, 2, 4, 1, 2, 3, 3, 2, 1, 2 ,3, 1]
# print(list(set(my_list)))
#
# new_list = list(set(my_list))
# print(new_list)

new_list = []
for i in my_list:
    if i in new_list:
         pass
    else:
         new_list.append(i)

print(new_list)


