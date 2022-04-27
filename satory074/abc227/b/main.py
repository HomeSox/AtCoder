import math
import collections as cl
from collections import deque

N = int(input())
S = list(map(int, input().split()))

ans = N
for s in S:
    is_correct = False
    for a in range(1, 1001):
        for b in range(1, 1001):
            men = 4 * a * b + 3 * a + 3 * b

            if men == s:
                is_correct = True
                break

            if men > s:
                break

    ans -= is_correct

print(ans)
