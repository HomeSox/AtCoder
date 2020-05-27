#!/usr/bin/env python3

N = int(input())
T = sorted([int(input()) for _ in range(N)])
T.reverse()

if len(T) == 1:
    print(T[0])
    exit()
elif len(T) == 2:
    print(T[0])
    exit()

T1 = [T[0]]
T2 = [T[1]]



for i in range(2, N):
    if sum(T1) < sum(T2):
        T1.append(T[i])
    else:
        T2.append(T[i])



if sum(T1) > sum(T2):
    print(sum(T1))
else:
    print(sum(T2))

