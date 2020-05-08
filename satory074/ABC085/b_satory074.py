import collections
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
d = [int(input()) for i in range(N)]
print(len(collections.Counter(d)))