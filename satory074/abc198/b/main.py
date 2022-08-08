import collections as cl
from collections import deque

N = input()

for i in range(100):
    s = f"{N[::-1]}{'0'*i}"
    if s == s[::-1]:
        print("Yes")
        break
else:
    print("No")
