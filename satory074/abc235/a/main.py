import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

abc = input()
bca = abc[1] + abc[2] + abc[0]
cab = abc[2] + abc[0] + abc[1]

print(int(abc) + int(bca) + int(cab))


