import collections as cl

N = int(input())
A = list(map(int, input().split()))

clc = cl.Counter(A)
sum_ = sum(A)

Q = int(input())
for _ in range(Q):
    B, C = map(int, input().split())

    sum_ += (C - B) * clc[B]

    clc[C] += clc[B]
    clc[B] = 0

    print(sum_)

