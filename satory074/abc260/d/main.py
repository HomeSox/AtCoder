import collections as cl
import math
import bisect

N, K = map(int, input().split())
P = list(map(int, input().split()))

yama = []
omote = []
ans = [0] * (N + 1)

for i, p in enumerate(P):
    idx = bisect.bisect_left(omote, p)

    if idx == len(omote):
        yama.append([p])
        omote.insert(idx, p)
    else:
        yama[idx].append(p)
        omote[idx] = p

    if len(yama[idx]) == K:
        omote.pop(idx)
        for y in yama.pop(idx):
            ans[y] = i + 1
        continue

for a in ans[1:]:
    if a == 0:
        print(-1)
    else:
        print(a)
