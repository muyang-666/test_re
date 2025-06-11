# 1，类实例化的方式
# 1.1 定义空元组(元组不能改变)
my_tuple1 = tuple()
print(type(my_tuple1),my_tuple1) #<class 'tuple'> ()

# 1.2 类型转化
# 可以将列表转化为元组， 只需要将 [], 变为 ()，同时也能反向转化
my_tuple2 = tuple([1, 2, 3])
print(my_tuple2) #(1, 2, 3)
# 转化字符串
my_tuple3 = tuple('hello')
print(my_tuple3) #('h', 'e', 'l', 'l', 'o')

# 2. 直接使用 () 定义
my_tuple4 = (1,"小木",3.14,True)
print(my_tuple4)
print(my_tuple4[1]) #小木

# 3. 特殊点 ：定义只有一个数据的元组时，数据后面必须有一个逗号
my_tuple5 =  (1,)
print(my_tuple5) #(1,)

