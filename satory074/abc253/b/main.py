H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]

maru = []
for i, l in enumerate(S):
    for j, s in enumerate(l):
        if s == "o":
            maru.append((i, j))

print(abs(maru[0][0] - maru[1][0]) + abs(maru[0][1] - maru[1][1]))
