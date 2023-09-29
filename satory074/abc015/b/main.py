N = int(input())
A = list(map(int, input().split()))

import math

n = 0
for a in A:
    if a > 0:
        n += 1

print(math.ceil(sum(A) / n))
