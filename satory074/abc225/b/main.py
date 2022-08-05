import math
import collections as cl
from collections import deque

N = int(input())
ab = [tuple(map(int, input().split())) for _ in range(N - 1)]
ab = set(ab)
chouten = [a_ for a_, _ in ab] + [b_ for _, b_ in ab]

clc = cl.Counter(chouten)

for k, v in clc.items():
    if v == (N - 1):
        exit(print("Yes"))

print("No")
