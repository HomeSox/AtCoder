#!/usr/bin/env python3

N = int(input())
NG = [int(input()) for _ in range(3)]

numbers = [0]

for i in range(1, N+1):
    if i in NG: continue
    numbers.append(i)

n_123 = [1, 2, 3]
print(numbers)
if N in NG:
    print('NO')
else:
    index = len(numbers)-1
    print(index)
    cnt = 0
    while index > 0:
        print('index',index)
        f = True
        for i in range(3, 0, -1):
            print('index-i', index-i)
            if index-i < 0: continue
            print('chinko', numbers[index-i])
            if numbers[index]-numbers[index-i] in n_123:
                index -= i
                print('unko,',index, numbers[index])
                f = False
                break
        cnt += 1
        if cnt == 100:
            print('NO')
            exit()
        if f == True:
            print('NO')
            exit()
        if index == 0:
            print('YES')
            exit()

print('NO')
