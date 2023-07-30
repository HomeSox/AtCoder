import collections as cl
import math

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

ans = []
for h in range(N - 8):
    for w in range(M - 8):
        # print(S[h][w], end="")

        if not S[h][w] == S[h][w + 1] == S[h][w + 2] == "#":
            continue

        if not S[h + 1][w] == S[h + 1][w + 1] == S[h + 1][w + 2] == "#":
            continue

        if not S[h + 2][w] == S[h + 2][w + 1] == S[h + 2][w + 2] == "#":
            continue

        if not S[h + 3][w] == S[h + 3][w + 1] == S[h + 3][w + 2] == S[h + 3][w + 3] == ".":
            continue

        if not S[h][w + 3] == S[h + 1][w + 3] == S[h + 2][w + 3] == ".":
            continue

        if not S[h + 5][w + 5] == S[h + 5][w + 6] == S[h + 5][w + 7] == S[h + 5][w + 8] == ".":
            continue

        if not S[h + 6][w + 6] == S[h + 6][w + 7] == S[h + 6][w + 8] == "#":
            continue

        if not S[h + 7][w + 6] == S[h + 7][w + 7] == S[h + 7][w + 8] == "#":
            continue

        if not S[h + 8][w + 6] == S[h + 8][w + 7] == S[h + 8][w + 8] == "#":
            continue

        if not S[h + 6][w + 5] == S[h + 7][w + 5] == S[h + 8][w + 5] == ".":
            continue

        ans.append((h + 1, w + 1))

ans.sort()

for k, v in ans:
    print(k, v)
