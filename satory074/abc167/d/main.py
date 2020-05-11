#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
n, k = map(int, input().split())
a = list(map(int, input().split()))
a = [a_ - 1 for a_ in a]
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

"""
ord_ = [-1] * n # 何回目に訪れたか
homon = [] # 訪問した順番のリスト
current = 0
while ord_[current] == -1:
    ord_[current] = len(homon)
    homon.append(current)
    current = a[current] - 1

freq = len(homon) - ord_[current] # ループする都市数
n_before_loop = ord_[current] # ループするまでの都市数

if k < n_before_loop:
    print(homon[k] + 1)
else:
    k -= n_before_loop
    k %= freq
    print(homon[n_before_loop+k] + 1)
"""

ord_ = [-1] * n # 何回目に訪れたか
homon = [] # 訪問した順番のリスト
current = 0
while ord_[current] == -1:
    ord_[current] = len(homon)
    homon.append(current)
    current = a[current]

D = [ord_]
for _ in range(int(math.log2(n))):
    d = []

print(ord_)
