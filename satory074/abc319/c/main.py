import collections as cl
import math

c = [list(map(int, input().split())) for _ in range(3)]

# cを1次元にする
c = [c[0][0], c[0][1], c[0][2], c[1][0], c[1][1], c[1][2], c[2][0], c[2][1], c[2][2]]

n_gakkari = 0


def is_gakkari(l):
    if l[0] != l[1]:
        return False

    if l[0] == l[2]:
        return False
    else:
        return True


# 9までのすべての順列を生成
import itertools

permutations = list(itertools.permutations(list(range(9))))

n_gakkari = 0
for perm in permutations:
    yoko1 = []
    yoko2 = []
    yoko3 = []
    tate1 = []
    tate2 = []
    tate3 = []
    naname1 = []
    naname2 = []
    for l_ in perm:
        if l_ == 0:
            yoko1.append(c[l_])
            tate1.append(c[l_])
            naname1.append(c[l_])
            continue

        if l_ == 1:
            yoko1.append(c[l_])
            tate2.append(c[l_])
            continue

        if l_ == 2:
            yoko1.append(c[l_])
            tate3.append(c[l_])
            naname2.append(c[l_])
            continue

        if l_ == 3:
            yoko2.append(c[l_])
            tate1.append(c[l_])
            continue

        if l_ == 4:
            yoko2.append(c[l_])
            tate2.append(c[l_])
            naname1.append(c[l_])
            naname2.append(c[l_])
            continue

        if l_ == 5:
            yoko2.append(c[l_])
            tate3.append(c[l_])
            continue

        if l_ == 6:
            yoko3.append(c[l_])
            tate1.append(c[l_])
            naname2.append(c[l_])
            continue

        if l_ == 7:
            yoko3.append(c[l_])
            tate2.append(c[l_])
            continue

        if l_ == 8:
            yoko3.append(c[l_])
            tate3.append(c[l_])
            naname1.append(c[l_])
            continue

    if is_gakkari(yoko1):
        n_gakkari += 1
        continue

    if is_gakkari(yoko2):
        n_gakkari += 1
        continue

    if is_gakkari(yoko3):
        n_gakkari += 1
        continue

    if is_gakkari(tate1):
        n_gakkari += 1
        continue

    if is_gakkari(tate2):
        n_gakkari += 1
        continue

    if is_gakkari(tate3):
        n_gakkari += 1
        continue

    if is_gakkari(naname1):
        n_gakkari += 1
        continue

    if is_gakkari(naname2):
        n_gakkari += 1
        continue


print(1 - (n_gakkari / len(permutations)))
