#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
n, m  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

q = 2 ** m
#print(n, m, 3800 * q, (n - m) * q)
print((1900 * m) * q + 100 * (n - m) * q)
