A, B, K = map(int, input().split())

l = []
for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        l.append(i)

print(l[::-1][K-1])
