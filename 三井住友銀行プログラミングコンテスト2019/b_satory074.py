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

N = int(input())
if int(math.ceil(N / 1.08) * 1.08) == N:
    print(int(math.ceil(N / 1.08)))
else:
    print(":(")