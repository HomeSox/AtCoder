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

H = int(input())

c = 0
for i in range(10000000):
    c += 1
    if H == 1:
        break
    else:
        H = H // 2

ans = 0
for i in range(c):
    ans += 2 ** i

print(ans)