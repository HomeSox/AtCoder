N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

ans = N
total = 0
for i, a in enumerate(A):
    total += a
    if total > X:
        break

ans = min(i + 1, ans)

total = 0
for i, b in enumerate(B):
    total += b
    # c2 += 1
    if total > Y:
        break

ans = min(i + 1, ans)

print(ans)
