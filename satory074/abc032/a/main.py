import math
import collections as cl
from collections import deque

a = int(input())
b = int(input())
n = int(input())

for i in range(n, 10 ** 9):
    if i % a == 0 and i % b == 0:
        print(i)
        break
