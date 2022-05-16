import math
import collections as cl
from collections import deque

N = int(input())
A = list(map(int, input().split()))

ma = 0
mi = 10 ** 9 + 1
for a in A:
    if a > ma:
        ma = a

    if a < mi:
        mi = a

print(ma - mi)
# print(max(A) - min(A))

