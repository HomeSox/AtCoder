import collections as cl
import math

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for a in A:
        if a % 2 == 1:
            ans += 1

    print(ans)
