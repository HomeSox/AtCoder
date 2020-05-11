#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
s  = input()
t  = input()
#  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()
print('Yes' if s == t[:-1] else 'No')
