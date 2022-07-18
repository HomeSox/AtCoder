import collections as cl
import math

N = int(input())
r = input()

sum_ = 0
for s in r:
    if s == "A":
        sum_ += 4
        continue

    if s == "B":
        sum_ += 3
        continue

    if s == "C":
        sum_ += 2
        continue

    if s == "D":
        sum_ += 1
        continue

print(sum_ / N)
