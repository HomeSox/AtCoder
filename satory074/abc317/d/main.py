N = int(input())
XYZ = [list(map(int, input().split())) for _ in range(N)]

sumZ = sum(Z for X, Y, Z in XYZ)

dp = [float('inf') for _ in range(sumZ + 1)]
dp[0] = 0

for x, y, z in XYZ:
    w = (y - x + 1) // 2 if x < y else 0

    for i in range(sumZ, z - 1, -1):
        dp[i] = min(dp[i], dp[i - z] + w)

print(min(dp[(sumZ + 1) // 2:]))
