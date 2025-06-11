# 1. 使用 类实例化的方法

my_dict = dict()
print(type(my_dict), my_dict) #<class 'dict'> {}

# dict() 不能转化列表和元组，字符串

# 2.直接使用{} 定义
# 2.1 空字典
my_dict1 = {}
print(type(my_dict1), my_dict1) #<class 'dict'> {}

# 2.2 非空字典
my_dict2 = {"name":['小木','木木'],"age":18,"height":1.69,"man":True}
print(my_dict2) #{'name': '小木', 'age': 18, 'height': 1.69, 'man': True}

# 添加信息 like
my_dict2['like'] = 'play'
print(my_dict2)

# 修改年龄为 19
my_dict2['age'] = 19
print(my_dict2) #{'name': ['小木', '木木'], 'age': 19, 'height': 1.69, 'man': True, 'like': 'play'}

# 3. 添加一个爱好， 学习-->本质是向列表中添加一个数据
my_dict2['name'].append('木秧')
print(my_dict2) #{'name': ['小木', '木木', '木秧'], 'age': 19, 'height': 1.69, 'man': True, 'like': 'play'}