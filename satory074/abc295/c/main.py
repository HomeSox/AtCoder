import collections as cl
import math

N = int(input())
A = list(map(int, input().split()))

clc = cl.Counter(A)
ans = 0
for k, v in clc.most_common():
    ans += v // 2

print(ans)

