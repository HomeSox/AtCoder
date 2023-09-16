import collections as cl
import math

S = input()

ans = -1
for i in range(len(S) + 1):
    for j in range(i + 1, len(S) + 1):
        s = S[i:j]

        if s == s[::-1]:
            ans = max(ans, len(s))

print(ans)