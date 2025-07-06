# with open('b.txt', encoding='utf-8') as f:
#     buf = f.readline() #111
#     print(buf)
#     print(f.readline()) #222


with open('b.txt',encoding='utf-8') as f:
    for i in f:
        print(i, end='')
        