'''
猫类，属性 name, age ,show_info(输出属性信息)
'''

class Cat:
    # 定义添加属性的方法
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'小猫的名字是： {self.name},年龄是: {self.age}')
        
# 创建对象, Cat
blue_cat =Cat('蓝猫',2)

blue = blue_cat
blue.show_info()
