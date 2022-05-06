import math
import collections as cl
from collections import deque

N = int(input())
C = list(map(int, input().split()))
MOD = 1000000007

C.sort()

ans = 1
for i in range(N):
    ans = ans * max(0, C[i] - i) % MOD

print(ans)

