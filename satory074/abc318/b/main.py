import collections as cl
import math

N = int(input())

n_covered = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    A, B, C, D = map(int, input().split())

    for i in range(A, B):
        for j in range(C, D):
            n_covered[i][j] += 1

ans = 0
for i in range(101):
    for j in range(101):
        if n_covered[i][j] >= 1:
            ans += 1

print(ans)