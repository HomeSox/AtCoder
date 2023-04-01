import math

N = int(input())
NG = [int(input()) for _ in range(3)]

if N in NG:
    print("NO")
    exit()

dp = [math.inf for _ in range(N + 1)]
dp[N] = 0

for i in range(N, -1, -1):
    if dp[i] == -1:
        continue

    for j in range(1, 4):
        n = i - j

        if n < 0:
            break

        if n in NG:
            continue

        c = min(dp[n], dp[i] + 1)

        if c > 100:
            continue

        dp[n] = c

# print(dp)
print("NO" if dp[0] == math.inf else "YES")
