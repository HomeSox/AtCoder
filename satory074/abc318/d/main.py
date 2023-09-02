N = int(input())

D = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(i + 1, N):
        D[i][j] = row[j - i - 1]

dp = [0] * (1 << N)

for b in range((1 << N) - 1):
    l = None
    for i in range(N):
        if (b >> i) & 1 == 0:
            l = i
            break

    for i in range(N):
        if (b >> i) & 1 == 0:
            nb = b | (1 << l) | (1 << i)
            dp[nb] = max(dp[nb], dp[b] + D[l][i])

print(dp[-1])
