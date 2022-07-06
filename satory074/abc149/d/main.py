N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

ans = 0
for j in range(K):
    L = T[j::K]

    dp = [{"hand": "", "point": 0} for _ in range(len(L) + 1)]
    for i in range(len(L)):
        if L[i] == "r":
            if dp[i]["hand"] == "p":
                dp[i + 1]["hand"] = ""
                dp[i + 1]["point"] = dp[i]["point"]
            else:
                dp[i + 1]["hand"] = "p"
                dp[i + 1]["point"] = dp[i]["point"] + P
        elif L[i] == "s":
            if dp[i]["hand"] == "r":
                dp[i + 1]["hand"] = ""
                dp[i + 1]["point"] = dp[i]["point"]
            else:
                dp[i + 1]["hand"] = "r"
                dp[i + 1]["point"] = dp[i]["point"] + R
        elif L[i] == "p":
            if dp[i]["hand"] == "s":
                dp[i + 1]["hand"] = ""
                dp[i + 1]["point"] = dp[i]["point"]
            else:
                dp[i + 1]["hand"] = "s"
                dp[i + 1]["point"] = dp[i]["point"] + S

    ans += dp[-1]["point"]

print(ans)
