import collections as cl
import math

N = int(input())
A = list(map(int, input().split()))


index_ = [[0, -1, i] for i in range(N+1)]

for i, a in enumerate(A):
    c, idx, n = index_[a]


    if c == 1:
        index_[a] = [2, i+1, n]
    else:
        index_[a] = [c + 1, idx, n]

# print(index_)


ans = [n for c, idx, n in sorted(index_[1:], key=lambda x: x[1])]
print(*ans)


