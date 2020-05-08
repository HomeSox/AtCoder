A = int(input())
B = int(input())

list = [A, B]

for i in range(1, 4):
    if i not in list:
        print(i)
        exit()
