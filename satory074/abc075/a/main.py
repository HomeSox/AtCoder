#!/usr/bin/env python3
import collections
import itertools as it
import math

#import numpy as np

#  = input()
#  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

A, B, C = map(int, input().split())
ABC = [A, B, C]
ABC.sort()

l = []
for n in ABC:
    if n in l:
        if len(l) == 1:
            print(ABC[-1])
        else:
            print(l[0])
        exit()
    else:
        l.append(n)
