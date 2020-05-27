#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
h, w = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

sharp = []
p = 0
for _ in range(h):
    ipt = list(input())
    print(ipt[p:])
    for i in range(p, w):
        if ipt[i] == '#':
            p = i
            break
    else:
        print('Impossible')
        break
else:
    print('Possible')

