import math
import collections as cl
from collections import deque

a, b, c = map(int, input().split())

clcm = cl.Counter([a, b, c]).most_common()
n = clcm[0][1]

if n == 1:
    print(0)
if n == 2:
    print(clcm[1][0])
if n == 3:
    print(clcm[0][0])
