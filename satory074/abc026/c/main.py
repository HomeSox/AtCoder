import collections as cl
import math

N = int(input())
joushi = [-1 for _ in range(N + 1)]
buka = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    B = int(input())

    joushi[i] = B
    buka[B].append(i)

kyuuryou = [1 for _ in range(N + 1)]
for i in range(N, 0, -1):
    if not buka[i]:
        continue

    kl = [kyuuryou[b_] for b_ in buka[i]]
    kyuuryou[i] = max(kl) + min(kl) + 1

# print(joushi)
# print(buka)
# print(kyuuryou)

print(kyuuryou[1])