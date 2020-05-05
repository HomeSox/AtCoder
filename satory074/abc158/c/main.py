#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
a, b = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()


for i in range(0, 10**7):
    if int(i * 0.08) == a and int(i * 0.1) == b:
        print(i)
        break
else:
    print(-1)
