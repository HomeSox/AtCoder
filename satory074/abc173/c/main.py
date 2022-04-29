import collections as cl
import math

H, W, K = map(int, input().split())
C = [input() for _ in range(H)]

ans = 0
for i in range(2 ** H):
    for j in range(2 ** W):
        c_black = 0
        for h in range(H):
            for w in range(W):
                if C[h][w] == "#":
                    if not ((i >> h) & 1 or (j >> w) & 1):
                        c_black += 1

        if c_black == K:
            ans += 1

print(ans)
