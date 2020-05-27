#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
l = input().split()
n = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

for _ in range(n):
    q = input()

    for i in range(len(l)):
        if len(l[i]) == len(q):
            if '*' in q:
                for s1, s2 in zip(l[i], q):
                    if s2 != '*' and s1 != s2:
                        break
                else:
                    l[i] = '*' * len(l[i])
            else:
                if l[i] == q:
                    l[i] = '*' * len(l[i])

print(' '.join(l))
