#!/usr/bin/env python3
import collections as cl
from math import factorial

def comb(n, r):
    if n >= r:
        return factorial(n) // (factorial(n - r) * factorial(r))
    else:
        return 0
  
n = int(input())
a = list(map(int, input().split()))

clc = cl.Counter(a)

# 1. 数字が等しいペアを選ぶ総数
npair = 0
for (k, v) in clc.items():
    npair += comb(v, 2)

# 2. (取り除いた数字と同じ数字を選ぶ総数) - (1)
for a_ in a:
    print(npair - (clc[a_] - 1))
