#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
s  = input()
#  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

max_ = -1
for tail in range(2, len(s)):
    s_ = s[:tail]
    if len(s) % 2 == 0 and s_[:len(s_)//2] == s_[len(s_)//2:]: 
        max_ = max(max_, len(s_))

print(max_)
