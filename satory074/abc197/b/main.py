import collections as cl
import math

H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1


S = [list(input()) for _ in range(H)]
# print(S)

ans = 0
for i in range(X, -1, -1):
    if S[i][Y] == ".":
        ans += 1
    else:
        break
    # print(S[i][Y])

for i in range(X, H):
    if S[i][Y] == ".":
        ans += 1
    else:
        break
    # print(S[i][Y])

for i in range(Y, -1, -1):
    if S[X][i] == ".":
        ans += 1
    else:
        break
    # print(S[X][i])

for i in range(Y, W):
    if S[X][i] == ".":
        ans += 1
    else:
        break
    # print(S[X][i])

print(ans - 3)
