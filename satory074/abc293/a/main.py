import collections as cl
import math

S = input()

ans = ''
for i in range(len(S) // 2):
    ans += S[i*2 + 1]
    ans += S[i*2]

print(ans)