"""
You are given an integer N. If N is between −2
31
  and 2
31
 −1 (inclusive), print Yes; otherwise, print No.
"""

import collections as cl

N = int(input())

if -(2**31) <= N < 2**31:
    print("Yes")
else:
    print("No")
