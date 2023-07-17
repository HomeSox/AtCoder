import collections as cl
import math

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

ans = []
for i, b_ in enumerate(b):
    n = a[0] ^ b_

    l = [a_ ^ n for a_ in a]
    l.sort()

    if l == b:
        ans.append(n)

ans = sorted(list(set(ans)))

print(len(ans))
for ans_ in ans:
    print(ans_)