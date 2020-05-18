#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
a, b, c, d  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

nlcmc = b // c
nlcmd = b // d
nlcmcd = b // lcm(c, d)
nb = b - (nlcmc + nlcmd - nlcmcd)

a -= 1
nlcmc = a // c
nlcmd = a // d
nlcmcd = a // lcm(c, d)
na = a - (nlcmc + nlcmd - nlcmcd)

print(nb - na)
