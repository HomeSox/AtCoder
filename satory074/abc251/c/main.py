import collections as cl
import math

N = int(input())

depu = {}
pt = 0
ans = 0
for i in range(N):
    S, T = list(input().split())
    try:
        depu[S]
    except:
        depu[S] = int(T)

        if int(T) > pt:
            pt = int(T)
            ans = i + 1

print(ans)
