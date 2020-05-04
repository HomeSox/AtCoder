#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
s  = input()
n = len(s)
#  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

def is_kaibun(s):
    l = len(s)
    s1 = s[:(l-1)//2]
    s2 = s[(l+3)//2-1:]

    return (s == s[::-1]), s1, s2

is_kaibun_, s1, s2 = is_kaibun(s)

if is_kaibun_:
    q1 = s[:(n-1)//2]
    is_kaibun1, s1, s2 = is_kaibun(q1)
    #print(is_kaibun(q1))
    q2 = s[(n+3)//2-1:]
    is_kaibun2, s1, s2 = is_kaibun(q2)
    #print(is_kaibun(q2))
    print('Yes' if is_kaibun1 * is_kaibun2 else 'No')
else:
    print('No')
