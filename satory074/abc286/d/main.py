import collections as cl
import math

N, X = map(int, input().split())


kouka = {}
A = []
for i in range(N):
    a, b = map(int, input().split())
    kouka[a] = b

dp = [0] * (X + 1)
for a, b in kouka.items():
    l = []
    for b_ in range(b):
        if a * (b_ + 1) > X:
            break

        l.append(a * (b_ + 1))

    for dpi, dp_ in enumerate(dp):
        if dp_ == 0:
            continue

        for b_ in range(b):
            if dpi + a * (b_ + 1) > X:
                break

            l.append(dpi + a * (b_ + 1))

    for l_ in l:
        dp[l_] = 1


if dp[-1] == 1:
    print("Yes")
else:
    print("No")
