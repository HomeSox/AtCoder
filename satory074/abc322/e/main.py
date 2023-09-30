N, K, P = map(int, input().split())
plans = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] = i個の開発案でパラメータ設定jを満たす最小コスト
dp = [{tuple([0] * K): 0} for _ in range(N + 1)]

for i in range(1, N + 1):
    C, *A = plans[i - 1]
    new_dp = dict(dp[i - 1])

    for param, c in dp[i - 1].items():
        new_param = [0 for _ in range(K)]
        for j in range(K):
            new_param[j] = min(param[j] + A[j], P)

        key_ = tuple(new_param)

        # 最小コストを更新
        new_dp[key_] = min(new_dp.get(key_, float("inf")), c + C)

    dp[i] = new_dp

# 目標パラメータ
target = tuple([P] * K)

# 最小コストを求める
min_cost = float("inf")
for i in range(N + 1):
    cost = dp[i].get(target, float("inf"))

    if cost < min_cost:
        min_cost = cost

if min_cost == float("inf"):
    print(-1)
else:
    print(int(min_cost))
