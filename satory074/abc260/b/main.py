import collections as cl
import math

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

jukensei = [(i, a, b, a + b) for i, a, b in zip(range(N), A, B)]

is_gokaku = [False] * N

cnt = 0
for i, a, b, c in sorted(jukensei, reverse=True, key=lambda x: x[1]):
    if cnt == X:
        break
    is_gokaku[i] = True

    cnt += 1

cnt = 0
for i, a, b, c in sorted(jukensei, reverse=True, key=lambda x: x[2]):
    if cnt == Y:
        break

    if not is_gokaku[i]:
        is_gokaku[i] = True
        cnt += 1

cnt = 0
for i, a, b, c in sorted(jukensei, reverse=True, key=lambda x: x[3]):
    if cnt == Z:
        break

    if not is_gokaku[i]:
        is_gokaku[i] = True
        cnt += 1

for i, b in enumerate(is_gokaku):
    if b:
        print(i + 1)
