import collections as cl
import math

H, W, rt, ct = map(int, input().split())

N = int(input())


grid = [["." for _ in range(W)] for _ in range(H)]

for i in range(N):
    r, c = map(int, input().split())
    r = r - 1
    c = c - 1
    print(r, c)
    grid[r][c] = "#"


[print(r) for r in grid]
