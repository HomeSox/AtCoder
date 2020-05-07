#!/usr/bin/env python3

N = int(input())
NG = [int(input()) for _ in range(3)]

for i in range(100):
    if N in NG:
        print('NO')
        exit()

    if N - 3 not in NG:
        N -= 3
    elif N - 2 not in NG:
        N -= 2
    else:
        N -= 1

if N <= 0:
    print('YES')
else:
    print('NO')
