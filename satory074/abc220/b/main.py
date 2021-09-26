K = int(input())
A, B = map(int, input().split())

A10 = 0
for i, a in enumerate(list(str(A))[::-1]):
    A10 += K ** i * int(a)

B10 = 0
for i, b in enumerate(list(str(B))[::-1]):
    B10 += K ** i * int(b)

print(A10 * B10)