import collections as cl
import math

N = int(input())
a = list(map(int, input().split()))
a.sort()

clc = cl.Counter(a)

daburi = 0
for k, v in clc.items():
    daburi += v - 1

is_having = [False for _ in range(2 * N + 1)]

for a_ in a:
    if a_ > N:
        continue

    is_having[a_] = True

a = list(set(a))
a.sort()
sale_idx = N - 1
for i in range(1, 2 * N + 1):
    # print(i, a)
    if is_having[i]:
        continue

    if daburi >= 2:
        daburi -= 2
        continue

    if daburi == 1:
        daburi -= 1

        if len(a) < 1:
            print(i - 1)
            exit()
        else:
            sale_target = a[-1:]
    else:
        if len(a) < 2:
            print(i - 1)
            exit()
        else:
            sale_target = a[-2:]

    for n in sale_target:
        if n < i:
            print(i - 1)
            exit()

    for n in sale_target:
        a.pop(-1)
        if n > N:
            continue
        is_having[n] = False

    is_having[i] = True
