import collections
import itertools as it
import math
import numpy as np

# A = input()
# A = int(input())
# A = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for i in range(N)]
#
# c = collections.Counter()

N, S, T = map(int, input().split())
kg = int(input())

cnt = 0
for i in range(N-1):
    if S <= kg <= T:
       cnt += 1

    kg += int(input())

if S <= kg <= T:
   cnt += 1

print(cnt)