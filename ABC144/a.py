import collections
import numpy as np

# = input()
# = int(input())
# = map(int, input().split())
# = list(map(int, input().split()))
#

N = int(input())

ans = 'No'
for i in range(9):
  for j in range(9):
    if (i + 1) * (j + 1) == N:
      ans = 'Yes'

print(ans)
