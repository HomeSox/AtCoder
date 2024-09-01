N, X = map(int, input().split())
A = list(map(int, input().split()))

is_know = [False] * N

while True:
    if is_know[X - 1]:
        break

    is_know[X - 1] = True
    X = A[X - 1]

print(sum(is_know))
