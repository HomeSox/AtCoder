import collections as cl
import math

N, P, Q, R, S = map(int, input().split())
P -= 1
Q -= 1
R -= 1
S -= 1
A = list(map(int, input().split()))

ans = []
for i in range(N):
    # print(i)
    if P <= i <= Q:
        ans.append(A[R + i - P])
    elif R <= i <= S:
        ans.append(A[i - R + P])
    else:
        ans.append(A[i])

print(*ans)
