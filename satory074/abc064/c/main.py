#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
n  = int(input())
#  = map(int, input().split())
a  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#

colors = [a_ // 400 for a_ in a if a_ < 3200]
colors_3200 = [a_ // 400 for a_ in a if a_ >= 3200]
c = collections.Counter(colors)

min_ = len(c) if c else 1
max_ = len(c) + len(colors_3200)
print(min_, max_)
