import collections as cl
import math

N = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(2 * N + 2)]
for i, a in enumerate(A):
    idx = i + 1
    ans[idx * 2] = ans[a] + 1
    ans[idx * 2 + 1] = ans[a] + 1

for a in ans[1:]:
    print(a)
