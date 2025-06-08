list1 = [1,3,5,7,2,3]

# 找 数据 3 出现的下标
num = list1.index(3)
print(num) # 1

# 找数据 4 出现的下标
# num = list1.index(4) # 报错
if 4 in list1:
    num1 = list.index(4)
    print(num1)
else:
    print('不存在 4')