import collections as cl
import math

# W = int(input())
W = 10**7

ans = [1, 2, 3]

for i in range(W + 1):
    if sum(ans[-3:]) < i:
        ans.append(sum(ans[-3:]))

print(len(ans))
print(*ans)
