N, K = map(int, input().split())
A = list(map(int, input().split()))

p = []
for i in range(N):
    p.append([A[i], -i])

p.sort()

ans = 10 ** 10
max_ = -1
for a, i in p:
    if -i < K:
        max_ = max(max_, -i)
    else:
        if max_ == -1:
            continue

        ans = min(ans, -i - max_)

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)

