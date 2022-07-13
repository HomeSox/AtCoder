import collections as cl
import math

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ma = max(A)

for i, a in enumerate(A):
    if ma == a:
        None
    else:
        continue

    if i + 1 in B:
        print("Yes")
        break
else:
    print("No")
