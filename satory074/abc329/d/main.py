import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * (N + 1)  # 各候補者の得票数
ans = 0  # 現時点での当選者
results = []

for vote in A:
    cnt[vote] += 1
    if cnt[ans] < cnt[vote]:
        ans = vote
    elif cnt[ans] == cnt[vote]:
        ans = min(ans, vote)

    print(ans)


