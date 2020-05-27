#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
n = int(input())
#  = map(int, input().split())
t = [int(input()) for i in range(n)]
#
# c = collections.Counter()

if n == 1:
    print(t[0])
elif n == 2:
    print(max(t))
elif n == 3:
    t = sorted(t)[::-1]
    ma = t.pop(0)
    print(max(ma, sum(t)))
else:
    t = sorted(t)[::-1]
    ma = t.pop(0)
    t = sorted(t)
    mi = t.pop(0)

    joken1 = max(ma + mi, sum(t)) # 2 - 2: お前は51で合ってるよ♡
    #print(ma, mi, min(t))
    joken2 = max(ma, mi + sum(t)) # 3 - 1: お前は50だろ！
    #print(joken1, joken2) # 1, 2, 3, 50
    print(min(joken1, joken2))
