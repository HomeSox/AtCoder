import collections as cl
import math

S = input()

awesome = "atcoder"
l = [awesome.index(s) for s in S]


def get_inversion_count(l):
    count = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                count += 1
    return count


print(get_inversion_count(l))
