N = int(input())
A = list(map(int, input().split()))

l = []
for a1, a2 in zip(A[:-1], A[1:]):
  for i in range(a1, a2, (a2 - a1) // abs(a2 - a1)):
    l.append(i)

l.append(A[-1])

print(*l)
