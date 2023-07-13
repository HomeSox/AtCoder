import collections as cl
import math
from collections import deque

N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]

ans = 0

ans += N
X -= sum(m)

ans += X // min(m)

print(ans)