import collections

# A = input()
# A = int(input())
# A = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for i in range(N)]
#
# c = collections.Counter()

N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = [tuple(map(int, input().split())) for i in range(M)]

cl = collections.Counter(A)
BC += [(cl[key], key) for key in cl]
BC = sorted(BC, key=lambda x: -x[1])

c = 0
total = 0
for (n, key) in BC:
  if (c + n) < N:
    c += n
    total += key * n
  else:
    total += key * (N - c)
    break

print(total)
