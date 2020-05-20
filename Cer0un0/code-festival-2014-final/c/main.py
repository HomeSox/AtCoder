#!/usr/bin/env python3

A = int(input())

cnt = 0

for i in range(10, 10**5):
    S = list(str(i))
    S.reverse()
    p = 0
    cnt += 1
    f = 0
    for s in S:
        f += int(s)*(i**p)
        p += 1
    if f == A:
        print(i)
        exit()
    if f > 10**16:
        break

print(-1)
    
