import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
S = input()

n_able_muji = M
n_able_logo = 0
ans = 0
for s in S:
    if s == "0":
        n_able_muji = M
        n_able_logo = ans

    if s == "1":
        if n_able_muji > 0:
            n_able_muji -= 1
        else:
            if n_able_logo > 0:
                n_able_logo -= 1
            else:
                ans += 1

        continue

    if s == "2":
        if n_able_logo > 0:
            n_able_logo -= 1
        else:
            ans += 1

        continue

print(ans)




