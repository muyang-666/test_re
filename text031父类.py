class Dog:
    def bark(self):
        print('汪汪汪叫....')
        print('汪汪汪叫....')

class XTQ(Dog):
    # XTQ 类bark 方法不再是汪汪汪叫, 改为 嗷嗷嗷叫
    # 1.先 嗷嗷嗷叫(新功能) 2, 汪汪汪叫(父类功能) 3.嗷嗷嗷叫(新功能)
    def bark(self):
        print('嗷嗷嗷叫....')
        super().bark()
        print('嗷嗷嗷叫...')

xtq = XTQ()
xtq.bark()