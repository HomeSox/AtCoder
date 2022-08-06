import collections as cl
import math

Y = int(input())

for i in range(4):
    if (Y + i) % 4 == 2:
        print(Y + i)
        break
