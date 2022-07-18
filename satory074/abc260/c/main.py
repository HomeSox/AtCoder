import collections as cl
import math

N, X, Y = map(int, input().split())


def crash_blue(blevel):
    if blevel == 1:
        return 1

    return crash_red(blevel - 1) + crash_blue(blevel - 1) * Y


def crash_red(rlevel):
    if rlevel == 1:
        return 0

    return crash_red(rlevel - 1) + crash_blue(rlevel) * X


print(crash_red(N))
