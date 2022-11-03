import collections as cl
import math

N = int(input())
A = list(map(int, input().split()))

max_o1 = -1
max_o2 = -1
max_e1 = -1
max_e2 = -1
for i, a in enumerate(A):
    if a % 2 == 0:
        if a > max_e2:
            mi = min(a, max_e1)
            ma = max(a, max_e1)
            max_e2 = mi
            max_e1 = ma
    else:
        if a > max_o2:
            mi = min(a, max_o1)
            ma = max(a, max_o1)
            max_o2 = mi
            max_o1 = ma

# print(max_o1, max_o2, max_e1, max_e2)

l = []
for n in [max_o1, max_o2, max_e1, max_e2]:
    if n == -1:
        continue
    l.append(n)

ans = -1
for i in range(len(l)):
    for j in range(len(l)):
        if i == j:
            continue

        if (l[i] + l[j]) % 2 == 0:
            ans = max(ans, l[i] + l[j])

print(ans)
