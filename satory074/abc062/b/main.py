#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
h, w  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

print(f'{"#" * (w + 2)}')
for _ in range(h):
    print(f'#{input()}#')
print(f'{"#" * (w + 2)}')
