import collections as cl
import math

S = input()

if "a" in S:
    ans = -1
    for i, s in enumerate(S):
        if s == "a":
            ans = i

    print(ans + 1)
else:
    print(-1)
