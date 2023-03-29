import collections as cl
import math

L, N1, N2 = map(int, input().split())
row1 = [list(map(int, input().split())) for _ in range(N1)]
row2 = [list(map(int, input().split())) for _ in range(N2)]

# print(row1)
# print(row2)
# print()

i, j = 0, 0
ans = 0

while i < N1 and j < N2:
    # print(row1[i])
    # print(row2[j])
    # print()

    if row1[i][0] == row2[j][0]:
        ans += min(row1[i][1], row2[j][1])

    if row1[i][1] < row2[j][1]:
        row2[j][1] -= row1[i][1]
        i += 1

        if row2[j][1] == 0:
            j += 1

        continue

    if row1[i][1] > row2[j][1]:
        row1[i][1] -= row2[j][1]
        j += 1

        if row1[i][1] == 0:
            i += 1

        continue

    if row1[i][1] == row2[j][1]:
        i += 1
        j += 1

        continue

print(ans)