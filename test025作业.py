my_list = []

for i in range(3):
    my_dict = {}
    name = input('请输入名字:')
    age = input('请输入年龄:')
    my_dict['name'] = name
    my_dict['age'] = age
    my_list.append(my_dict)

for item in my_list:
    print(item['name'],item['age'])