import collections as cl
import math

N = int(input())
p = list(map(int, input().split()))

happy_head_index = [0] * N

for i, p_ in enumerate(p):
    head = ((p_ - i) + N) % N
    happy_head_index[(head - 1 + N) % N] += 1
    happy_head_index[head] += 1
    happy_head_index[(head + 1) % N] += 1

print(max(happy_head_index))
