N = int(input())
P = list(map(int, input().split()))

ans = 1
index = P[0]

for i in range(1, N):
    if index > P[i]:
        index = P[i]
        ans += 1


print(ans)
