#!/usr/bin/env python3

K = int(input())

if K <= 9:
    print(K)
    exit()

num = []

for i in range(10, 100):
    s = str(i)
    if int(s[0]) <= int(s[1]):
        continue
    num.append(i)

if K < len(num):
    print(num[K-10])
    exit()

n = len(num) + 9

while n < K:
    array = []
    cnt = 0
    for i in range(1, 10):
        for n2 in num:
            s = str(n2)
            if int(i) <= int(s[0]):
                break
            ret = int(str(i)+s)
            array.append(ret)
            n += 1
            if n == K:
                print(ret)
                exit()
    n += cnt
    num = array
