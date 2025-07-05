"""
需求： 小猫爱吃鱼，小猫要喝水，定义不带属性的类
"""

class Cat:
    def eat(self):
        print("小猫爱吃鱼。。。")

    def drink(self):
        print('小猫要喝水。。。')

# 2. 创建对象
blue_cat = Cat()
# 3. 通过对象调用类中的方法
blue_cat.eat()
blue_cat.drink()