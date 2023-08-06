import collections as cl
import math

N = int(input())
P = list(map(int, input().split()))

if N == 1:
    print(0)
    exit()

max_ = max(P[1:])

if max_ < P[0]:
    print(0)
else:
    print(max_ - P[0] + 1)
