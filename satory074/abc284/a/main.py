import collections as cl
import math

N = int(input())

l = []
for _ in range(N):
    l.append(input())

for l_ in l[::-1]:
    print(l_)
