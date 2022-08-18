import math
import collections as cl
from collections import deque

n, k = input().split()

ans = 0
for n_ in range(1, int(n)+1):
  for k_ in range(1, int(k)+1):
    ans += int(f"{n_}0{k_}")

print(ans)
