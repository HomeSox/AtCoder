N = int(input())
A = list(map(int, input().split()))

last_seen = {}
ans = float("inf")

for i in range(N):
    if A[i] in last_seen:
        ans = min(ans, i - last_seen[A[i]] + 1)
    last_seen[A[i]] = i

print(-1 if ans == float("inf") else ans)
