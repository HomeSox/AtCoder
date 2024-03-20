import collections as cl
import math
import sys
from collections import Counter, deque

sys.setrecursionlimit(10 ** 6)

S = input()
cnt = Counter(S)


same = False  # 同じ文字が2回以上含まれているかどうか

n = len(S)
ans = n * n - sum(c * c for c in cnt.values())
ans //= 2

if len(S) != len(cnt):
    ans += 1

print(ans)
