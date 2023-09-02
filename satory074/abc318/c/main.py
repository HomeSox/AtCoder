import collections as cl
import math

N, D, P = map(int, input().split())
F = list(map(int, input().split()))

F.sort(reverse=True)

ans = sum(F)
for i in range(0, len(F), D):
    total = sum(F[i:i + D])

    if P <= total:
        ans -= total - P
    else:
        break

print(ans)
