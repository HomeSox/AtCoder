#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
a, b = input().split()
#  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()


max_ = int(a) - int(b)
for i in range(6):
    for n in range(10):
        s = list(a) + list(b)
        s[i] = str(n)
        a_ = int(''.join(s[:3]))
        b_ = int(''.join(s[3:]))

        if a_ - b_ > max_ and s[0] != '0' and s[3] != '0':
            max_ = a_ - b_

print(max_)
