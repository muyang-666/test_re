# 定义列表

mylist = [1,3,5,7]

#  1. 想要将下标为 1 的数据修改为22
mylist[1] = 22
print(mylist) # [1, 22, 5, 7]

# 修改最后一个位置的数据， 改为 'hello'
mylist[-1] = 'hello'
print(mylist) #[1, 22, 5, 'hello']

# 2.如果指定下标不存在，会报错
# mylist[10] = 10 #报错