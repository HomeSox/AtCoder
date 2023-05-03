N = int(input())
T = list(map(int, input().split()))

sum_ = sum(T)
dp = [False for _ in range(sum_ + 1)]
dp[0] = True
for t in T:
    for i in range(sum_, t - 1, -1):
        if dp[i - t]:
            dp[i] = True

ans = sum_
for i, d in enumerate(dp):
    if d:
        ans = min(ans, max(i, sum_ - i))

print(ans)
