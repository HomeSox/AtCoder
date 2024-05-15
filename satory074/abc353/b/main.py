N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
aki = K
for a in A:
  if a <= aki:
    aki -= a
  else:
    ans += 1
    aki = K - a

print(ans + (0 if aki == K else 1))
