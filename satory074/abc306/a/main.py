import collections as cl
import math

N = int(input())
S = input()

ans = ''
for s in S:
    for _ in range(2):
        ans += s

print(ans)
