#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
x  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

n11 = (x // 11)
rest = x - n11 * 11
rest6 = int(bool(rest % 6))
rest5 = int(bool(rest // 6 % 5))
#print(n11, rest, rest6, rest5)
print(n11 * 2 + rest6 + rest5)
