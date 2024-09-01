N, K = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(K):
    a = A.pop()
    A = [a] + A

print(*A)
