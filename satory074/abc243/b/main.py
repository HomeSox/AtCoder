import collections as cl
import math

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = 0
ans2 = 0
for a, b in zip(A, B):
    if a == b:
        ans1 += 1
    else:
        if a in B:
            ans2 += 1

print(ans1)
print(ans2)
