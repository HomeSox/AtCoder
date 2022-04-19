import math
import collections as cl
from collections import deque

s = input()
k = int(input())

if len(s) < k:
    print(0)
    exit()

passwords = []
for i in range(len(s) - k + 1):
    # print(s[i : i + k])
    if s[i : i + k] not in passwords:
        passwords.append(s[i : i + k])

print(len(passwords))
