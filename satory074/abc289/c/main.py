import collections as cl
import math

N, M = map(int, input().split())
S = []

for _ in range(M):
    C = input()
    S.append(list(map(int, input().split())))

ans = 0
for bit in range(1 << M):
    S_ = []
    for i in range(M):
        if bit & (1 << i):
            S_ += S[i]


    S_ = sorted(list(set(S_)))

    if len(S_) != N:
        continue

    for i, s in zip(range(1, N+1), S_):
        if i != s:
            break
    else:
        ans += 1
        # print(S_)

print(ans)