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
N, K = map(int, input().split())
H = list(map(int, input().split()))

H.sort()

rest = sum(H[::-1][K:])

print(rest)