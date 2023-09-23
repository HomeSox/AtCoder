N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(101):
    l = A + [i]

    score = sum(l) - max(l) - min(l)

    if score >= X:
        print(i)
        exit()

print(-1)