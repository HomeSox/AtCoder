N, K = map(int, input().split())
a = list(map(int, input().split()))

def get_sum(B, l, r):
    """累積和を使用して配列の特定の範囲[l, r]の合計を返す"""

    res = B[r]
    if l > 0:
        res -= B[l - 1]

    return res

Q = [0] * N
Q[0] = a[0]

# 累積和
for i in range(1, N):
    Q[i] = Q[i - 1] + a[i]

ans = 0
R = 0

for L in range(N):
    R = max(R, L)

    # 累積和を使って、条件を満たす範囲を探す
    while R < N and get_sum(Q, L, R) < K:
        R += 1

    ans += N - R

print(ans)