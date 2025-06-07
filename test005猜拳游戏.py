import random


while True:
    palyer = int(input("石头为1，剪刀为2，布为3，退出为0，请输入:"))
    if palyer == 0:
        break
    compter = random.randint(1,3)
    if compter == 1:
        str1 = "石头"
    if compter == 2:
        str1 = "剪刀"
    if compter == 3:
        str1 = "布"

    if (palyer == 1 and compter == 2)or(palyer == 2 and compter == 3)or(palyer == 3 and compter == 1):
        print(f"你赢了compter为{str1}")
    elif palyer == compter:
        print("平局")
    else:
        print(f"你输了,compter为{str1}")