import collections as cl
import math

N = int(input())

for n in range(N, 1000):
    s = str(n)

    if int(s[0]) * int(s[1]) == int(s[2]):
        print(n)
        exit()