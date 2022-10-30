import collections as cl
import math

N = int(input())
H = list(map(int, input().split()))

ans = 0
ma = -1
for i, h in enumerate(H):
    if h > ma:
        ma = h
        ans = i + 1
print(ans)
