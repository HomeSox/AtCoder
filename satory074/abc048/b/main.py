#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
a, b, x  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

ans = b // x - a // x
ans += 1 if a % x == 0 else 0
#ans += 1 if b % x == 0 else 0
print(ans)
