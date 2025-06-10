mylist = [1,3,5,7,9,2,4,6,8,0]

# 1. 删除最后一个位置的数据
mylist.pop() #默认删除最后一个
print(mylist) #[1, 3, 5, 7, 9, 2, 4, 6, 8]

# 2. 删除最下标为 1 的数据 3
mylist.pop(1)
print(mylist) #[1, 5, 7, 9, 2, 4, 6, 8]

# 3. 删除数据为7 的数据
mylist.remove(7)
print(mylist) #[1, 5, 9, 2, 4, 6, 8]

# 4. 清空
mylist.clear()
print(mylist)