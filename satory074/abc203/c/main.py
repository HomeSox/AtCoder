import math
import collections as cl
from collections import deque

N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()

ans = K
for i in range(N):
    if ans >= AB[i][0]:
        ans += AB[i][1]

print(ans)
