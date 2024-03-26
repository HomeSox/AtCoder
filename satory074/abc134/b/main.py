N, D = map(int, input().split())

nsee = D * 2 + 1
print(N // nsee + min(N % nsee, 1))
