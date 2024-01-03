import collections as cl
import math
from collections import deque

a, b = input().split()
n = int(a + b)

for i in range(1000):
    if i ** 2 == n:
        print("Yes")
        exit()

print("No")
