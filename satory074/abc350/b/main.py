N, Q = map(int, input().split())
T = list(map(int, input().split()))

l = [True for _ in range(N + 1)]

for t in T:
  l[t] = not l[t]

print(sum(l) - 1)
