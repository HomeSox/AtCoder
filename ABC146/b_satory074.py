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
S = input()



for s in S:
    # print(ord('A'))
    print(chr(((ord(s) + N) - 65) % 26 + 65), end="")