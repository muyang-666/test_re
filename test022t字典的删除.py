my_dict2 = {"name":['小木','木木'],"age":18,"height":1.69,"man":True}

# 删除 man 键对
del my_dict2['man']
print(my_dict2) # {'name': ['小木', '木木'], 'age': 18, 'height': 1.69}

# 字典.pop('键')
my_dict2.pop('age')
print(my_dict2) # {'name': ['小木', '木木'], 'height': 1.69}

# 删除木木 名字 ,删除列表中的值
my_dict2['name'].pop(1)
print(my_dict2) # {'name': ['小木'], 'height': 1.69}

# 清空键值对
my_dict2.clear()
print(my_dict2) # {}