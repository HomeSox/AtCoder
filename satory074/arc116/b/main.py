N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

A.sort(reverse=True)

ans = 0
s = 0
for a in A:
    ans += a * (a + s)
    ans %= MOD
    s = (s * 2 + a) % MOD

print(ans)
