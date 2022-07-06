A, B, K = map(int, input().split())

tak_eat = min(A, K)
aok_eat = min(B, K - tak_eat)

print(A - tak_eat, B - aok_eat)
