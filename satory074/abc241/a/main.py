import collections as cl
import math

a = list(map(int, input().split()))

k = 0
ans = a[0]
for _ in range(2):
    ans = a[ans]
    k = ans

print(ans)
