import numpy as np

n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

ans = np.inf
for a1, a2 in zip(a[:-1], a[1:]):
    v = a2 - a1
    if v < ans:
        ans = v

print(ans)