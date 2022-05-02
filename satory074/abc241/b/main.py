import collections as cl
import math

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

clc = cl.Counter(A)

for b in B:
    if clc[b]:
        clc[b] -= 1
    else:
        print("No")
        break
else:
    print("Yes")

