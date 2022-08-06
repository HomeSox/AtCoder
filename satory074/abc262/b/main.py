import collections as cl
import math

N, M = map(int, input().split())
li = [[False for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    U, V = map(int, input().split())

    li[U][V] = True
    li[V][U] = True


ans = 0
for i in range(1, N - 1):
    for j in range(i, N):
        for k in range(j, N + 1):
            if li[i][j] and li[j][k] and li[k][i]:
                ans += 1

print(ans)
