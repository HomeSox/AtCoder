H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

dp = [[0] * W for _ in range(H)]

for i in range(H):
    dp[i][0] = 1

for j in range(W):
    dp[0][j] = 1

for i in range(1, H):
    for j in range(1, W):
        if A[i][j] != A[i-1][j] and A[i][j] != A[i][j-1]:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

def f(m, i, j, path, l):
    path.append(m[i][j])

    if i == len(m) - 1 and j == len(m[0]) - 1:
        l.append(path[:])

    if j + 1 < len(m[0]):
        f(m, i, j+1, path, l)

    if i + 1 < len(m):
        f(m, i+1, j, path, l)

    path.pop()

paths = []
f(A, 0, 0, [], paths)

ans = 0
for p in paths:
    if len(set(p)) == len(p):
        ans += 1

print(ans)
