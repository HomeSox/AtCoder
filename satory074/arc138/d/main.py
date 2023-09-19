N, K = map(int, input().split())
A = list(map(int, input().split()))

p = []
for i in range(N):
    p.append([A[i], -i])

p.sort(reverse=True)

print(p)


