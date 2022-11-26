import collections as cl
import math

A, B = map(int, input().split())

'''
g = 1
t = 0
for i in range(10):
    t = B * i + (A / (g ** (1/2)))

    print(g, t)

    g += 1
'''

def f(x):
    return B * x + (A / ((x+1) ** (1/2)))


g = 1
l = 0
r = 10 ** 18
# 三分探索
while g < 10000:
    c1 = (l * 2 + r) // 3
    c2 = (l + r * 2) // 3

    # print(g, l, r, f(l), f(r))

    g += 1

    if f(c1) > f(c2):
        l = c1
    else:
        r = c2

print(min(f(l), f(r), f((l+r)//2)))
