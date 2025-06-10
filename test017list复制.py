mylist = [1,2,3]

list1 = mylist[:]
print(mylist)
print(list1)
list1[1] = 22
print(mylist)
print(list1)

print('-'*30)


list2 = mylist.copy()
print(mylist)
print(list2)
list2[1] = 32
print(mylist)
print(list2)

