N, L, R = map(int, input().split())
A = list(map(int, input().split()))
rA = A[::-1]

f = [0 for _ in range(N + 1)]
for i in range(N):
    f[i + 1] = min(f[i] + A[i], L * (i + 1))

g = [0 for _ in range(N + 1)]
for i in range(N):
    g[i + 1] = min(g[i] + rA[i], R * (i + 1))

# print(f)
# print(g)

ans = 10**18
for i in range(N + 1):
    ans = min(ans, f[i] + g[N - i])

print(ans)
