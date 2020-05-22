#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
n, x  = map(int, input().split())
a  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

b = f'{x:len(a)b}'

ans = 0
print(b)
for i in range(min(len(b), len(a))):
    if b[i] == '1':
       ans += a[i] 

print(ans)

