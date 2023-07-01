from decimal import Decimal

N = int(input())

l = []
for i in range(N):
    A, B = map(str, input().split())
    rate = Decimal(Decimal(A) / (Decimal(A) + Decimal(B)))

    l.append([rate, N - i, i + 1])


l.sort()
l.reverse()

ans = []
for i in range(N):
    ans.append(l[i][2])

print(*ans)


