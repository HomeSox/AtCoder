import collections as cl
import math

N = int(input())
l = {}
for i in range(N):
    S = input()

    if S in l:
        print(f"{S}({l[S]})")
        l[S] += 1
    else:
        print(S)
        l[S] = 1
