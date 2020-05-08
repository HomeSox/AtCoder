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

M1, D1 = map(int, input().split())
M2, D2 = map(int, input().split())

lastd = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if D2 == 1:
    print(1)
else:
    print(0)