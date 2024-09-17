N = int(input())
A = list(map(int, input().split()))

ans = N
pre = 0
souwa = lambda n: n * (n + 1) // 2
for i in range(1, N - 1):
    if A[i] - A[i - 1] != A[i + 1] - A[i]:
        ans += souwa(i - pre)
        pre = i

ans += souwa(N - 1 - pre)
print(ans)
