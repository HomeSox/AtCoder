import collections as cl
import math

H, W = map(int, input().split())
S = [input() for i in range(H)]

wmin = W - 1
wmax = 0
hmin = H - 1
hmax = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            if j < wmin:
                wmin = j
            if j > wmax:
                wmax = j
            if i < hmin:
                hmin = i
            if i > hmax:
                hmax = i


for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            if wmin <= j <= wmax and hmin <= i <= hmax:
                print(i + 1, j + 1)
                exit()
