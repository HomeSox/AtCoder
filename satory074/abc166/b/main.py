#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
n, k  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

snuke = [0] *n

for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for idx in a:
        snuke[idx-1] += 1    

ans = 0
for snuke_ in snuke:
    if snuke_ == 0:
        ans += 1

print(ans)
