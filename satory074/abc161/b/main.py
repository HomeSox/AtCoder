import bisect
import itertools


def generate_numbers(n, k):
    pos = range(n)
    for p in itertools.combinations(pos, k):
        number = 0

        for p_ in p:
            number |= 1 << p_

        yield number


l = list(generate_numbers(60, 3))
l.sort()

T = int(input())
for t in range(T):
    N = int(input())

    index = bisect.bisect_right(l, N)

    if index == 0:
        print(-1)
        continue
    else:
        print(l[index - 1])
