S = input()

MOD = 10**9 + 7
target = "chokudai"
dp = [0] * (len(target) + 1)
dp[0] = 1

for char in S:
    for j in range(len(target), 0, -1):
        if char == target[j - 1]:
            dp[j] = (dp[j] + dp[j - 1]) % MOD

print(dp[len(target)])
