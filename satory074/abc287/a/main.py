import collections as cl
import math

N = int(input())
total = 0
for i in range(N):
    s = input()

    if s == "For":
        total += 1

if N // 2 < total:
    print("Yes")
else:
    print("No")
