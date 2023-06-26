import collections as cl
import math

N = int(input())

ans1 = (N+1) - ((N+1) % 5)
ans2 = ans1 + 5
# print(ans1, ans2)

if abs(ans1 - N) < abs(ans2 - N):
    print(ans1)
else:
    print(ans2)