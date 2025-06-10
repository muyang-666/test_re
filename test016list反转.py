mylist = [1,3,5,7,9,2,4,6,8,0]

# 使用切片的方法反转，会得到一个新列表
list1 = mylist[::-1]
print('mylist: ',mylist)
print('list1: ',list1)

# 使用 reverse 方法，直接修改原列表】
mylist.reverse()
print("mylist: ",mylist)