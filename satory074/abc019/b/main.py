#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
s  = input()
#  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

ans = ''
q = s[0]
for s_ in s[1:]:
    if q[0] != s_:
        ans += q[0] + str(len(q))
        q = s_
    else:
        q += s_

print(ans + q[0] + str(len(q)))



