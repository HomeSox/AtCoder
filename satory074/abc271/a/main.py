import collections as cl
import math

N = int(input())

ans = hex(N)[2:].upper()

if len(ans) == 1:
    ans = "0" + ans

print(ans)
