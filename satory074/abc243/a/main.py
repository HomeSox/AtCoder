import collections as cl
import math

V, A, B, C = list(map(int, input().split()))

abc = [A, B, C]
ans = ["F", "M", "T"]
for i in range(10**9):
    if abc[i % 3] > V:
        print(ans[i % 3])
        break
    else:
        V -= abc[i % 3]
