import collections as cl
import math

S = [list(input()) for _ in range(9)]


def other_point(x1, y1, x2, y2):
    x3, y3 = x2 - y2 + y1, y2 + x2 - x1
    x4, y4 = x1 - y2 + y1, y1 + x2 - x1

    return (x3, y3), (x4, y4)


def is_ok(x, y):
    ret = 0 <= x < 9 and 0 <= y < 9
    ret = ret and S[x][y] == "#"
    return ret


ans = []
for x1 in range(9):
    for y1 in range(9):
        if not is_ok(x1, y1):
            continue

        for x2 in range(x1, 9):
            for y2 in range(y1, 9):
                if not is_ok(x2, y2):
                    continue

                if x1 == x2 and y1 == y2:
                    continue

                (x3, y3), (x4, y4) = other_point(x1, y1, x2, y2)

                if not is_ok(x3, y3):
                    continue

                if not is_ok(x4, y4):
                    continue

                # print((x1, y1), (x2, y2), (x3, y3), (x4, y4))
                l = sorted([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])
                if l not in ans:
                    ans.append(l)

print(len(ans))
