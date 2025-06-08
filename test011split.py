str1 = "hello word and itcast and itheima and Python"

result1 = str1.split('and')
print(result1) #['hello word ', ' itcast ', ' itheima ', ' Python']

# 2,将 str1 按照 and 字符进行拆分，拆分一次
result2 = str1.split('and',1)
print(result2) #['hello word ', ' itcast and itheima and Python']

# 3.按照空白字符进行拆分
result3 = str1.split()
print(result3) #['hello', 'word', 'and', 'itcast', 'and', 'itheima', 'and', 'Python']

# 4.按照空白字符拆分，一次
result4 = str1.split(maxsplit=1)
print(result4) #hello', 'word and itcast and itheima and Python']