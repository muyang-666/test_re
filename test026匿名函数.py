# 1. 定义一个匿名函数可以求两个数的乘积
func1 = lambda a, b: a * b

# 2. 定义一个匿名函数, 参数为字典，返回字典中的健为 age的值
func2 = lambda x: x.get('age')
func3 = lambda x: x['age']

print(func1(1, 2))
my_dict = {'name': 'mumu','age': 18}
print(func2(my_dict))
print(func3(my_dict))

