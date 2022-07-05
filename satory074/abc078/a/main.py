import math
import collections as cl
from collections import deque

X, Y = input().split()

if X > Y:
    print(">")
elif X < Y:
    print("<")
else:
    print("=")
