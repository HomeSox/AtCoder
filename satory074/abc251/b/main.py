import collections as cl
import math

N, W = map(int, input().split())
A = list(map(int, input().split()))

ans = []

for i1 in range(N):
    if A[i1] <= W:
        ans.append(A[i1])

    for i2 in range(N):
        if i1 == i2:
            continue

        if A[i1] + A[i2] <= W:
            ans.append(A[i1] + A[i2])

        for i3 in range(N):
            if i1 == i3 or i2 == i3:
                continue

            if A[i1] + A[i2] + A[i3] <= W:
                ans.append(A[i1] + A[i2] + A[i3])

# print(ans)
print(len(set(ans)))
