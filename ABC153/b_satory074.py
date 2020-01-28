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
H, N = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) >= H:
    print('Yes')
else:
    print('No')