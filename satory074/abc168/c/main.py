#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
a, b, h, m  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

mr = (m / 60) * 360
hr = ((h * 60 + m) % 720 / 720) * 360
#print(mr, hr)
r = abs(hr - mr)

print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(r))))
