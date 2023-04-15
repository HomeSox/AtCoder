import collections as cl
import math

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

def f(m):
    return list(zip(*m[::-1]))

for _ in range(4):
    B = f(B)

    is_ok = True
    for a, b in zip(A, B):
        for a_, b_ in zip(a, b):
            if a_ == 0:
                continue

            if a_ != b_:
                is_ok = False

    if is_ok:
        print('Yes')
        exit()


    # print(A)
    # print(B)
    # print()

print('No')