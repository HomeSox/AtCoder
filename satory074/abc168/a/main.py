#!/usr/bin/env python3
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

if str(n)[-1] == '3':
    print('bon')
elif str(n)[-1] in ['2', '4', '5', '7', '9']:
    print('hon')
else:
    print('pon')
