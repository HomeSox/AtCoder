import collections as cl
import math

N, M = map(int, input().split())

switch = [[] for _ in range(N)]
for i in range(M):
    l = list(map(int, input().split()))

    for l_ in l[1:]:
        switch[l_ - 1].append(i)

tentou = list(map(int, input().split()))

ans = 0
for i in range(2 ** N):
    b = bin(i)[2:].zfill(N)
    denkyuu = [0 for _ in range(M)]

    for j, b_ in enumerate(b):
        # print(j, b, switch, denkyuu)
        if b_ == "1":
            for sw in switch[j]:
                denkyuu[sw] += 1

    for d, t in zip(denkyuu, tentou):
        if d % 2 != t:
            break
    else:
        ans += 1

print(ans)
