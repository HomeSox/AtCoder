import collections as cl
import math

N  = int(input())
A = list(map(int, input().split()))

l = []
for a in A:
    if a % 2 == 0:
        l.append(a)

print(*l)
