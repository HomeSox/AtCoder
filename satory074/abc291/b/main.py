N = int(input())
X = list(map(int, input().split()))

X.sort()

print(sum(X[N:-N]) / (N * 3))
