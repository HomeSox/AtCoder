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
n = int(input())
a = list(map(int, input().split()))

for a_ in a:
  if a_ % 2 == 0:
    if a_ % 3 != 0 and a_ % 5 != 0:
      print('DENIED')
      break
else:
  print('APPROVED')
