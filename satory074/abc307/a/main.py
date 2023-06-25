import collections as cl
import math

N = int(input())
A = list(map(int, input().split()))

ans = 0
l = []
for i in range(len(A)):
    ans += A[i]

    if (i + 1) % 7 == 0:
        l.append(ans)
        ans = 0

print(*l)

