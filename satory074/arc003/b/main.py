import collections as cl
import math

N = int(input())
s = [input() for _ in range(N)]
rs = [s_[::-1] for s_ in s]

rs.sort()

for s_ in rs:
    print(s_[::-1])
