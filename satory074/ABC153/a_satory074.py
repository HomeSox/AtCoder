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
H, A = map(int, input().split())

c = 0
for i in range(1000000000):
    if H <= 0:
        break
    else:
        c += 1
        H -= A

print(c)