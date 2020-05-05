#!/usr/bin/env python3
#  = input()
#a  = int(input())
n, a, b = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

if a == 0:
  print(0)
elif n < (a + b):
  print(min(n, a))
else:
  nab = n // (a + b)
  ans = nab * a
  mod = n % (nab * (a + b))
  ans += min(mod, a)
  print(ans)
