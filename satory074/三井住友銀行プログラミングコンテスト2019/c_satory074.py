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

X = int(input())
nshohin = X // 100
amari = X % 100

print(0 if nshohin * 5 < amari else 1)