import collections as cl
import math

N, M = map(int, input().split())
ans = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    ans[A].append(B)
    ans[B].append(A)

for a in ans[1:]:
    print(len(a), *sorted(a))
