my_list = []
print(my_list) # []

# 1. 想列表中添加数据 彭于晏
my_list.append('彭于晏')
print(my_list)

# 2. 想列表中添加数据 刘亦菲
my_list.append('刘亦菲')
print(my_list)

# 3.在下标位置为 1 的位置添加数据 木木
my_list.insert(1,'木木')
print(my_list) #['彭于晏', '木木', '刘亦菲']

# 4. 定义新的列表 list1
list1 = ['木秧','小小木']
# 将 list1 中的数据逐个添加到 my_list 中
my_list.extend(list1)
print(my_list)

# 将 list1 作为一个整体添加到 my_list 中
my_list.append(list1)
print(my_list)
