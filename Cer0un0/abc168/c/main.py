#!/usr/bin/env python3
import math
A, B, H, M = map(int, input().split())

h = 30
h_m = 1/2
m = 6

x = A**2 + B**2 - 2*A*B*math.cos(math.radians(H*h+M*h_m-M*m))
print(math.sqrt(x))
