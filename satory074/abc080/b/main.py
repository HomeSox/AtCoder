#!/usr/bin/env pypy3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
n  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

wa = sum([int(s) for s in str(n)])

print('Yes' if n % wa == 0 else 'No')
