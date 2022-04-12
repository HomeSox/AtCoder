N, K = map(int, input().split())


K = abs(K)
P = [0 for _ in range(N * 2 + 1)]

for v in range(2, N * 2 + 1):
    P[v] = min(v - 1, N * 2 + 1 - v)

ans = 0
for i in range(K, N * 2 + 1):
    ans += P[i] * P[i - K]

print(ans)

