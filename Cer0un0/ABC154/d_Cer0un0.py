N, K = map(int, input().split())
P = list(map(int, input().split()))


kitaiti = {}

k = 1.0
for i in range(1, 1001):
    kitaiti[i] = k
    k += 0.5

index = 0

for i in range(K):
    index += kitaiti[P[i]]

s = index
ans = index

for i in range(1, len(P)-K+1):
    s = index - kitaiti[P[i-1]] + kitaiti[P[i+K-1]]
    if s > ans: ans = s
    index = s
print(ans)

