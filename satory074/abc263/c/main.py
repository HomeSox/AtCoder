import collections as cl
import itertools
import math

N, M = map(int, input().split())

l = list(range(1, M + 1))
l = itertools.permutations(l, N)

for v in l:
    # print(v)
    for n1, n2 in zip(v[:-1], v[1:]):
        if n2 <= n1:
            break
    else:
        print(*v)
