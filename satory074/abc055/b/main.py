#!/usr/bin/env python3
import collections
import itertools as it
import math

# import numpy as np

#  = input()
#  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

N = int(input())
MOD = 10**9 + 7

ans = 1
for i in range(N):
    ans *= i + 1
    ans %= MOD

print(ans)
