#!/usr/bin/env python3
import math
a, b, x = map(int, input().split())
V = a*a*b

if V/2 >= x: # 三角形
    c = 2 * x / a / b
    print(math.degrees(math.atan2(b,c)))
else: # 台形
    c = 2 * (V-x) / a / a
    print(math.degrees(math.atan2(c,a)))
