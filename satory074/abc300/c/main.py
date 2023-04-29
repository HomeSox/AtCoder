import collections as cl
import math

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]


ans = [0 for _ in range(min(H, W) + 1)]
for i in range(H):
    for j in range(W):
        if C[i][j] == ".":
            continue

        larm = 0

        while i - (larm + 1) >= 0 and i + (larm + 1) < H and j - (larm + 1) >= 0 and j + (larm + 1) < W:
            if (
                C[i - (larm + 1)][j - (larm + 1)] == "#"
                and C[i - (larm + 1)][j + (larm + 1)] == "#"
                and C[i + (larm + 1)][j - (larm + 1)] == "#"
                and C[i + (larm + 1)][j + (larm + 1)] == "#"
            ):
                larm += 1
            else:
                break

        if larm >= 1:
            ans[larm] += 1

print(*ans[1:])
